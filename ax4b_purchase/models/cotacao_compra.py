# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class CotacaoDeCompras(models.Model):
    _name = 'purchase.cotacao_compra'
    _description = 'Cotação de Compras'

    name = fields.Char()
    empresa = fields.Many2one("res.company")
    cd_empresa = fields.Many2one(related='empresa.partner_id', string="Empresa")
    inconterm = fields.Many2one("account.incoterms")
    cd_inconterm = fields.Char(related='inconterm.name', string="Inconterm")
    codigo_compras_title = fields.Text()
    cd_solitacao_cotacao = fields.Char('Número de Cotação',readonly=True)
    data_emissao = fields.Datetime()
    data_esperada = fields.Datetime()
    quantidade = fields.Integer()
    moeda = fields.Many2one('res.currency')
    solicitar_cofirmacao=fields.Boolean(string="Socilitar confirmação 1 dia(s) antes")
    situacao = fields.Selection([('Sdc', 'Sdc')])
    prioridade = fields.Selection([('0', 'Normal'), ('1', 'Urgent')], 'Priority', default='0', index=True)
    status = fields.Selection([
        ("SDC", "SDC"),
        ("SDCENVIADA", "SDCENVIADA"),
        ("PEDIDODECOMPRA", "PEDIDO DE COMPRA"),
    ], default = "SDC")

    produtos_da_cotacao = fields.One2many("purchase.produtos_cotacao","cotacao_de_compra",string="Produtos")
    fornecedores_da_cotacao = fields.One2many("purchase.fornecedores_cotacao","cotacao_de_compra",string="Fornecedores da Cotação")
    fornecedores_selecionado_cotacao = fields.One2many("purchase.fornecedores_selecionado_cotacao","cotacao_de_compra",string="Fornecedores Selecionado da Cotação")

    nome_do_poder = fields.Char(related='nota_de_reserva.x_studio_ds_poder_reserva')
    nome_do_orgao = fields.Char(related='nota_de_reserva.x_studio_nome_do_orgao_reserva')
    nome_da_unidade_orcamentaria = fields.Char(related='nota_de_reserva.x_studio_nome_da_unidade_oramentria_reserva')
    nome_da_fonte = fields.Char(related='nota_de_reserva.x_studio_nome_da_fonte')
    
    ano = fields.Char(related='nota_de_reserva.x_studio_ano_reserva')
    orgao = fields.Char(related='nota_de_reserva.x_studio_cd_orgao_reserva')   
    poder = fields.Char(related='nota_de_reserva.x_studio_poder')
    unidade_orcamentaria = fields.Char(related='nota_de_reserva.x_studio_unidade_oramentria_reserva')
    fonte = fields.Char(related='nota_de_reserva.x_studio_fonte_reserva')

    modalidade_de_compra = fields.Many2one('x_modalidade_de_compra')
    modalidade_de_compra_name = fields.Char(related='modalidade_de_compra.x_studio_cod_modalidade_compra')
    nota_de_reserva = fields.Many2one('x_nota_de_reserva')
    cronograma = fields.One2many(related='nota_de_reserva.x_studio_cronograma_reserva')


#     @api.constrains('fornecedores_da_cotacao')
#     def _constrains_fornecedores_da_cotacao(self):
#         if not self.fornecedores_da_cotacao or len(self.fornecedores_da_cotacao)==0:
#             raise ValidationError("Erro ao configura fornecedor da cotação.") 

    @api.model
    def create(self, vals):
        obj = super(CotacaoDeCompras, self).create(vals)
        number = self.env['ir.sequence'].get('x_cotacao_compras')
        obj.write({'cd_solitacao_cotacao': number})
        return obj

    def write(self, vals):
        res = super(CotacaoDeCompras, self).write(vals)
        for record in self:
            for produto in record.produtos_da_cotacao:
                self._cr.execute('update x_produto_requisicao set x_studio_situao=%s where id=%s', ("Em Processo", produto.produtorequisicaoid))                                  
       
        self.flush()
        self.invalidate_cache()
        return res


    def btn_enviar_email(self):
        for record in self:
            for fornecedor in record.fornecedores_da_cotacao:
                # fornecedores
                for produto in record.produtos_da_cotacao:
                    # codigo do produto produtos_requisicao
                    self._cr.execute('INSERT INTO fornecedores_selecionado_cotacao (cotacao_de_compra, fornecedores, produtos_cotacao) VALUES (%s,%s,%s)', (record.id, fornecedor.id,produto.produtos_requisicao.id))                                  
                    raise ValidationError("executado com sucesso")
    # @ api.model 
    # def fields_view_get (self, view_id = None, view_type = 'form', toolbar = False, submenu = False): 
    #     res = super ("purchase.cotacao_compra", self) .fields_view_get (view_id = view_id, 
    #                                              view_type = view_type, 
    #                                              toolbar = toolbar, 
    #                                              submenu = submenu) 


    #     return res
    


    #     template_obj = self.env['mail.template'].sudo().search([('name','=','Teste E-mail')], limit=1)
    #     base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        
    #     body_html = '<p>Dear Anderson,<br />\
    #         We request your feedback for the employee Anderson as part \
    #         of the Performance Review. Click on the link below to submit your \
    #         comments.</p><br /><p><a href=%s class="btn btn-danger">Employee Peer Feedback</a><br></p>'
        
    #     mail_values = {                        
    #         'body_html': body_html,
    #         'recipient_ids': 'anderson.peruci@ax4b.com'
    #     }
        
        # create_and_send_email = self.env['mail.mail'].create(mail_values).send() 

        # for peers in self.peer_employee_ids:
        #     _url = ''+ base_url +'/peer_feedback/'+ str(self.id) +'/'
        #     if peers.user_id.partner_id.id:

        #         if template_obj:
