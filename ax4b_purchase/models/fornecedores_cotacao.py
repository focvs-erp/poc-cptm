from odoo import  models, fields, api


class FornecedoresDaCotacao(models.Model):
   _name = 'purchase.fornecedores_cotacao'
   _description = 'Fornecedores da Cotação'
    
   name = fields.Char() 
   teste = fields.Char()
   prioridade = fields.Selection([('0', 'Normal'), ('1', 'Urgent')], 'Priority', default='0', index=True)
   cotacao_de_compra = fields.Many2one("purchase.cotacao_compra", invisible=True, string="Cotação de Compra")
   fornecedores = fields.Many2one("res.partner", string="fornecedores")
   #contact = fields.Char(related="vendors.name")
   contato = fields.One2many(related="fornecedores.child_ids", string="contato")
   email = fields.Char(related="fornecedores.email", string="email")
   telefone = fields.Char(related="fornecedores.phone", string="telefone") 
   celular = fields.Char(related="fornecedores.mobile", string="celular") 
   #nome_fornecedor = fields.Char(related="fornecedores.name")
   
   
   #   @api.model
   #   def Contato(self, vals):
   #      #for Lista in self:
   #      obj = super(FornecedoresDaCotacao, self).create(vals)
   #      lista = self.get('contato')
   #       obj.write({'contato': lista })
   #       return obj

         # @api.depends('fornecedores')
         # def Fornecedores_Contato(self)
         #    for record in self:
         #       record.contato
                  # for contato in record.contato:
                  #    record.teste = record.contato.name
            


   #    @api.model
   #    def Email(self, vals)
   #       obj = super(FornecedoresDaCotacao, self).create(vals)
   #       email = self.get('email')
   #       obj.write({'email': email })
   #       return obj

   #   @api.model
   #   def Telefone(self, vals)
   #      obj = super(FornecedoresDaCotacao, self).create(vals)
   #       telefone = self.get('telefone')
   #       obj.write({'telefone': telefone  })
   #       return obj

   #   @api.model
   #   def Celular(self, vals)
   #      obj = super(FornecedoresDaCotacao, self).create(vals)
   #      celular = self.get('celular')
   #      obj.write({'celular': celular })
   #       return obj



        