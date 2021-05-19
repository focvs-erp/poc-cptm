from odoo import models, fields, api


class CodigoMotivo(models.Model):
     _name = 'account.codigo_motivo'
     _description = 'Código de Motivo'
    
     name = fields.Char(string="Código")
     descricao = fields.Char(string="Descrição")
    