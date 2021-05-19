from odoo import models, fields, api


class Multa(models.Model):
     _name = 'account.multa'
     _description = 'Código de Multa'
    
     name = fields.Char(string="Código")
     descricao = fields.Char(string="Descrição")
     dias = fields.Integer(string="Dias")
     percentual = fields.Float(string="Percentual")
