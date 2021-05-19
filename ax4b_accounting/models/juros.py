from odoo import models, fields, api


class Juros(models.Model):
     _name = 'account.juros'
     _description = 'Código de Juros'
    
     name = fields.Char(string="Código")
     descricao = fields.Char(string="Descrição")
     calculo = fields.Integer(string="Cálculo de Juros por")
     percentual = fields.Float(string="Percentual")
     dia_mes = fields.Integer(string="Dia/Mês")
     carencia = fields.Integer(string="Dias Carência")   
     