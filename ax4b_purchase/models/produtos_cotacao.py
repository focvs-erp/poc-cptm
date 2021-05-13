from odoo import  models, fields, api

contato_array= []

class ProdutosDaCotacao(models.Model):
   _name = 'purchase.produtos_cotacao'
   _description = 'Produtos da Cotação'

   requisicao = fields.Many2one("purchase.x_requisicoes_de_compr", string="Requisição")
   produtos_requisicao = fields.Many2one("x_produto_requisicao", string="Contato")
  
   # email = fields.Char(related="contato_fornecedores.email", string="Email")
   # telefone = fields.Char(related="contato_fornecedores.phone", string="Telefone") 
   # celular = fields.Char(related="contato_fornecedores.mobile", string="Celular") 
  
   @api.onchange('requisicao')
   def _onchange_requisicao(self):
      for record in self:
         if record.requisicaon.id:
            return {'domain': {'requisicao': [('x_studio_many2one_field_oMlx9', '=', record.requisicao.id)]}}
         else:
            return {'domain': {'requisicao': []}}               
