from odoo import  models, fields, api

contato_array= []

class ProdutosDaCotacao(models.Model):
   _name = 'purchase.produtos_cotacao'
   _description = 'Produtos da Cotação'

   name = fields.Char(string="Produto da cotação") 
   
   cotacao_de_compra = fields.Many2one("purchase.cotacao_compra", invisible=True, string="Cotação de Compra")
   # requisicao = fields.Many2one("x_requisicoes_de_compr", string="Requisição")
   produtos_requisicao = fields.Many2one("x_produto_requisicao", string="Produto")

   quantidade = fields.Integer(related="produtos_requisicao.x_studio_quantidade", string="Quantidade")
   unidademedida = fields.Many2one(related="produtos_requisicao.x_studio_unidade_de_medida", string="Unidade") 
   # situacao = fields.Selection(related="produtos_requisicao.x_studio_situao", string="Situação") 
   # requisicao = fields.Many2one(related="produtos_requisicao.x_studio_unidade_de_medida", string="Unidade") 

   # @api.onchange('requisicao')
   # def _onchange_requisicao(self):
   #    for record in self:
   #       if record.requisicao.id:
   #          return {'domain': {'produtos_requisicao': [('x_studio_many2one_field_oMlx9', '=', record.requisicao.id)]}}
   #       else:
   #          return {'domain': {'produtos_requisicao': []}}               
