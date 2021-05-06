# -*- coding: utf-8 -*-

from odoo import models, fields, api


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
    modalidade_de_compra = fields.Many2one("x_modalidade_de_compra")
    nota_de_reserva = fields.Many2one("x_nota_de_reserva")
    cronograma = fields.One2many(related="nota_de_reserva.x_studio_cronograma_reserva")
    fornecedores_da_cotacao = fields.One2many("purchase.fornecedores_cotacao","cotacao_de_compra",string="Fornecedores da Cotação")

    

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
    
