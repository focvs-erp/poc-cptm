# -*- coding: utf-8 -*-

from odoo import models, fields, api


class baixa_estoque(models.Model):
    _name = 'cptm_custom.baixa_estoque'
    _description = 'cptm_custom.baixa_estoque'

    name = fields.Char()
    numero_requisicao = fields.Text(string = "Número da Requisição")
    
    tipo_requisicao = fields.Selection([('Consumo', 'Consumo'),('Ativo', 'Ativo'),('Insumo', 'Insumo')], string = "Tipo Requisição")
    dt_emissao = fields.Date(string = 'Data de Emissão')
    dt_lancamento = fields.Date(string = 'Data de Lançamento')
    justificativa = fields.Char(string = "Justificativa")
    priority = fields.Selection([('0', 'Normal'), ('1', 'Urgent')], 'Priority', default='0', index=True)
    quantidade = fields.Integer(string = "Quantidade")
    state = fields.Selection([
        ("PROVISÓRIO", "PROVISÓRIO"),
        ("AGUARDANDO", "AGUARDANDO"),
        ("PRONTO", "PRONTO"),
        ("CONCLUIDO", "CONCLUIDO"),
    ], default = "PROVISÓRIO")
    
#   cd_produto = fields.One2Many(string= "Código do Produto")
#   cd_modalidade_compras = fields.One2Many(string= "Modalidade de Compras")
#     valor_total = fields.Float(string = "Valor Total", compute="_valor_total", store=True)
#     valor_unitario = fields.Float(string = "Valor Unitario")
    
#     @api.depends('quantidade')
#         def _valor_total(self):
#             for record in self:
#                 record.valor_total = float(record.quantidade * record.valor_unitario)
            
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
