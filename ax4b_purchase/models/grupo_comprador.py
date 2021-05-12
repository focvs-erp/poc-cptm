from odoo import  models, fields, api

class GrupoComprador(models.Model):
   _name = 'purchase.grupo_comprador'
   _description = 'Grupo de Compradores'

   cd_grupo_comprador = fields.Char(string="Código grupo Comprador")
   ds_grupo_comprador = fields.Char(string="Descrição Grupo Comprador")
#    cd_ativo = fields.Char(string="Ativo")
   cd_ativo = fields.Boolean(string='Ativo', default=True)
   compradores = fields.Many2many('purchase.comprador')




