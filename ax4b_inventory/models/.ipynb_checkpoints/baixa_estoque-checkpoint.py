# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Baixa_Estoque(models.Model):
    _name = 'stock.baixa_estoque'
    _description = 'stock.baixa_estoque'

    numero_requisicao = fields.Text(string = "Número da Requisição")
    
    tipo_requisicao = fields.Selection([('Consumo', 'Consumo'),('Ativo', 'Ativo'),('Insumo', 'Insumo')], string = "Tipo Requisição")
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
    
    checkbox = fields.Boolean(string = "marque")
    
  
        
    
#   cd_produto = fields.One2Many(string= "Código do Produto")
#    valor_total = fields.Float(string = "Valor Total", compute="_valor_total", store=True)
#     valor_unitario = fields.Float(string = "Valor Unitario")
#     nome_requisicao = fields.related(string = "Nome da Requisição")
    
#     @api.depends('quantidade')
#         def _valor_total(self):
#             for record in self:
#                 record.valor_total = float(record.quantidade * record.valor_unitario)
