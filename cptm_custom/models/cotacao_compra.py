# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cotacao_compra(models.Model):
    _name = 'cptm_custom.cotacao_compra'
    _description = 'cptm_custom.cotacao_compra'

    
    name = fields.Char()
    codigo_compras_title = fields.Text()
    cd_solitacao_cotacao = fields.Text(string= "Número de Cotação")
    data_emissao = fields.Date()
    data_esperada = fields.Date()
    quantidade = fields.Integer()
    valor_imposto = fields.Integer()
    situacao = fields.Selection([('Sdc', 'Sdc')])
    priority = fields.Selection([('0', 'Normal'), ('1', 'Urgent')], 'Priority', default='0', index=True)
    state = fields.Selection([
        ("SDC", "SDC"),
        ("SDCENVIADA", "SDCENVIADA"),
        ("PEDIDODECOMPRA", "PEDIDO DE COMPRA"),
    ], default = "SDC")
   # valor_total = fields.Float(compute= "_value")
   # cd_moeda = fields.Monetary()
   # ds_empresa = fields.One2Many()
   # cd_modalidade_compras = fields.One2Many()
   #produtos_abas = fields.Related()
   # fornecedores_abas = fields.Related()
    #cd_requisicao = fields.Related()
    #cd_produto = fields.Related()
    #unidade_medida= fields.Related()
    #valor_unitario = fields.Related()
    # inconterm = fields.Related()
  
    
     #@api.depends('quantidade')
     #def _value(self):
      #   for record in self:
       #      record.valor_total = float(record.quantidade * record.valor_unitario)

    

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100