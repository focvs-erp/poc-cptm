# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Baixa_Estoque(models.Model):
    _name = 'stock.baixa_estoque'
    _description = 'stock.baixa_estoque'

    # numero_requisicao = fields.Text(string = "Número da Requisição")
    # numero_requisicao = fields.Char('My Sequence', readonly=True)

    numero_requisicao = fields.Char('Número da Requisição')

    # on create method
    @api.model
    def create(self, vals):
        obj = super(Baixa_Estoque, self).create(vals)
        number = self.env['ir.sequence'].get('code')
        obj.write({'numero_requisicao': number})
        return obj

    tipo_requisicao = fields.Selection([('Consumo', 'Consumo'),('Ativo', 'Ativo'),('Insumo', 'Insumo')], string = "Tipo da Requisição")
    dt_emissao = fields.Date(string = 'Data de Emissão')
    dt_lancamento = fields.Date(string = 'Data de Lançamento')
    justificativa = fields.Char(string = "Justificativa")
    priority = fields.Selection([('0', 'Normal'), ('1', 'Urgent')], 'Priority', default='0', index=True)
    quantidade = fields.Integer(string = "Quantidade")
    reservado = fields.Char(string = "Reservado")
    state = fields.Selection([
        ("PROVISÓRIO", "PROVISÓRIO"),
        ("AGUARDANDO", "AGUARDANDO"),
        ("PRONTO", "PRONTO"),
        ("CONCLUIDO", "CONCLUIDO"),
    ], default = "PROVISÓRIO")
    

    tabela_requisicao = fields.Many2one('x_requisicoes_de_compr', string = "Requisição")
    nome_da_requisicao_related = fields.Char(related='tabela_requisicao.x_studio_nome_da_requisio', string="Nome da Requisição")
    produtos_da_requisicao_related = fields.One2many(related='tabela_requisicao.x_studio_one2many_field_jwTT5', string="Produto da Requisição")  
        
#   cd_produto = fields.One2Many(string= "Código do Produto")
#    valor_total = fields.Float(string = "Valor Total", compute="_valor_total", store=True)
#     valor_unitario = fields.Float(string = "Valor Unitario")
#     nome_requisicao = fields.related(string = "Nome da Requisição")
    
#     @api.depends('quantidade')
#         def _valor_total(self):
#             for record in self:
#                 record.valor_total = float(record.quantidade * record.valor_unitario)

    # @api.model
    # def create(self, vals): 
    #     vals['numero_requisicao'] = self.env['ir.sequence'].next_by_code('x_baixa_estoque')
    #     return super(Baixa_Estoque, self).create(vals)