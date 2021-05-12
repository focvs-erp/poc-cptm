from odoo import  models, fields, api

class GrupoComprador(models.Model):
   _name = 'purchase.grupo_comprador'
   _description = 'Grupo de Compradores'

   cd_grupo_comprador = fields.Char(string="Codigo grupo Comprador")
   ds_grupo_comprador = fields.Char(string="Descrição grupo comprador")
   cd_ativo = fields = fields.Char(string="Ativo")
   cadastro_comprador = fields.Many2many('purchase.cadastro_comprador')




