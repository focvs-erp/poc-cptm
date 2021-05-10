from odoo import  models, fields, api


class FornecedoresDaCotacao(models.Model):
   _name = 'purchase.fornecedores_cotacao'
   _description = 'Fornecedores da Cotação'
    
   name = fields.Char() 
   prioridade = fields.Selection([('0', 'Normal'), ('1', 'Urgent')], 'Priority', default='0', index=True)
   cotacao_de_compra = fields.Many2one("purchase.cotacao_compra", invisible=True, string="Cotação de Compra")
   fornecedores = fields.Many2one("res.partner", string="fornecedores")
   #contact = fields.Char(related="vendors.name")
   contato = fields.One2many(related="fornecedores.child_ids", string="contato")
   email = fields.Char(related="fornecedores.email", string="email")
   telefone = fields.Char(related="fornecedores.phone", string="telefone") 
   celular = fields.Char(related="fornecedores.mobile", string="celular") 
   
   
   #  @api.model
   #  def Contact(self, vals)
   #      obj = super(FornecedoresDaCotacao, self).create(vals)
   #      Lista = self.get('contato','email','telelefone','celular')
   #      obj.write({'contato': Lista })
   #      return obj
        