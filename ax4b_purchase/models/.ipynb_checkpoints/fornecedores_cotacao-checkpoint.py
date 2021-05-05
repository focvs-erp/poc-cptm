from odoo import  models, fields, api


class FornecedoresDaCotacao(models.Model):
   _name = 'purchase.fornecedores_cotacao'
   _description = 'Fornecedores da Cotação'
    
   name = fields.Char() 
   priority = fields.Selection([('0', 'Normal'), ('1', 'Urgent')], 'Priority', default='0', index=True)
   cotacao_de_compra = fields.Many2one("purchase.cotacao_compra", invisible=True, string="Cotação de Compra")
   vendors = fields.Many2one("res.partner")
   #contact = fields.Char(related="vendors.name")
   contact = fields.One2many(related="vendors.child_ids")
   email = fields.Char(related="vendors.email")
   phone = fields.Char(related="vendors.phone") 
   mobile = fields.Char(related="vendors.mobile") 
