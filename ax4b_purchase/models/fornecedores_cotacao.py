from odoo import  models, fields, api

contato_array= []

class FornecedoresDaCotacao(models.Model):
   _name = 'purchase.fornecedores_cotacao'
   _description = 'Fornecedores da Cotação'

   name = fields.Char() 
   selecionado= fields.Boolean(string="Marcar")
   prioridade = fields.Selection([('0', 'Normal'), ('1', 'Urgent')], 'Priority', default='0', index=True)
   cotacao_de_compra = fields.Many2one("purchase.cotacao_compra", invisible=True, string="Cotação de Compra")
   fornecedores = fields.Many2one("res.partner", string="Fornecedores")
   contato_fornecedores = fields.Many2one("res.partner", string="Contato")

   email = fields.Char(related="contato_fornecedores.email", string="Email")
   telefone = fields.Char(related="contato_fornecedores.phone", string="Telefone") 
   celular = fields.Char(related="contato_fornecedores.mobile", string="Celular") 
  
   @api.onchange('fornecedores')
   def _onchange_fornecedore(self):
      for record in self:
         if record.fornecedores.id:
            return {'domain': {'contato_fornecedores': [('parent_id', '=', record.fornecedores.id)]}}
         else:
            return {'domain': {'contato_fornecedores': []}}               
