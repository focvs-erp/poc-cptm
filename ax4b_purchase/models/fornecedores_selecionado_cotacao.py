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
   desconto = fields.Monetary(string='desconto')
   valortotal = fields.Monetary(string='Valor Total', compute='_total')
   condicaopagamento = fields.Char("Condição de Pagamento")
   prazodeentrega = fields.Char("Prazo de Entrega")
   

   # @api.depends('precounitario', 'quantidade')
   # def _total(self):
   #    self.precounitario = float(self.precounitario)
   #    if(self.quantidade > 0.00):
   #       self.valortotal = self.precounitario * self.quantidade - self.desconto
   #    else: 
   #       self.desconto = 0


   # @api.onchange('fornecedores')
   # def _onchange_fornecedore(self):
   #    for record in self:
   #       if record.situacao_fornecedor == '2':
   #              raise ValidationError("Fornecedor bloqueado para transações")
   #       if record.fornecedores.id:
   #          return {'domain': {'contato_fornecedores': [('parent_id', '=', record.fornecedores.id)]}}
   #       else:
   #          return {'domain': {'contato_fornecedores': []}}
