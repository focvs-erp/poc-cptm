from odoo import  models, fields, api
from odoo.exceptions import UserError, ValidationError

contato_array= []

class FornecedoresSelecionadoDaCotacao(models.Model):
   _name = 'purchase.fornecedores_selecionado_cotacao'
   _description = 'Fornecedor Selecionado Da Cotação'

   name = fields.Char() 
   aceito= fields.Boolean(string="Aceito")
   cotacao_de_compra = fields.Many2one("purchase.cotacao_compra", invisible=True, string="Cotação de Compra")
   fornecedores = fields.Many2one("res.partner", string="Fornecedores")
   produtos_cotacao = fields.Many2one("purchase.produtos_cotacao", string="Produto")
   
   quantidade = fields.Integer(related="produtos_cotacao.quantidade", string="Quantidade")
   unidademedida = fields.Many2one(related="produtos_cotacao.unidademedida", string="Unidade") 
  
   currency_id = fields.Many2one('res.currency', string='Currency', required=True, readonly=True, states={'draft': [('readonly', False)]},
                                  default=lambda self: self.env.company.currency_id.id)
   
   precounitario = fields.Monetary(string='Valor Unitário')
   desconto = fields.Monetary(string='Desconto')
   valortotal = fields.Monetary(string='Valor Total', compute='_total')
   condicaopagamento = fields.Char("Condição de Pagamento")
   prazodeentrega = fields.Char("Prazo de Entrega")
   

   @api.depends('precounitario', 'quantidade','desconto')
   def _total(self):
      # if(self.quantidade > 0.00):
      #    self.precounitario = float(self.precounitario)
      # else:
      #    self.precounitario = 0

      if(self.quantidade > 0.00):
         self.valortotal = (self.precounitario * self.quantidade) - self.desconto
      else: 
         self.valortotal = 0

