from odoo import  models, fields, api

contacts = [('1', 'option1'), ('2', 'option2')]

class FornecedoresDaCotacao(models.Model):
   _name = 'purchase.fornecedores_cotacao'
   _description = 'Fornecedores da Cotação'
    
   name = fields.Char() 

   prioridade = fields.Selection([('0', 'Normal'), ('1', 'Urgent')], 'Priority', default='0', index=True)
   cotacao_de_compra = fields.Many2one("purchase.cotacao_compra", invisible=True, string="Cotação de Compra")
   fornecedores = fields.Many2one("res.partner", string="Fornecedores")
   #contact = fields.Char(related="vendors.name")
   contato_fornecedores = fields.One2many(related="fornecedores.child_ids", string="Contato")
   # escolha_de_contato = fields.Selection([('', 'record.contato_fornecedores.name'), ['4','Sem registros']],compute='_contato_fornecedores', store= True)
   teste = fields.Selection(contacts, string="Contato Fornecedor")
   # selecao_contato = fields.Char(compute='_selecao_contato', store=True)
   # email_contato_fornecedores = fields.Char(compute='_selecao_contato', store=True)
   # telefone_contato_fornecedores = fields.Char(compute='_selecao_contato', store=True)
   # celular_contato_fornecedores = fields.Char(compute='_selecao_contato', store=True)
   email = fields.Char(related="fornecedores.email", string="Email")
   telefone = fields.Char(related="fornecedores.phone", string="Telefone") 
   celular = fields.Char(related="fornecedores.mobile", string="Celular") 
   #nome_fornecedor = fields.Char(related="fornecedores.name")


   @api.depends('fornecedores')
   def _add_contato(self):
      #   contato_array= []
      #   teste_array = [('1', 'option1'), ('2', 'option2')]
      for record in self:
         if record.contato_fornecedores:
            for contato in record.contato_fornecedores:
               contacts.append(contato.name)
                  
      # return teste_array
        
   
   # @api.depends('fornecedores')
   # def _add_contato(self):
   #    contato_array= []
      
   #    return [('1', 'option1'), ('2', 'option2')]



   # @api.depends('contato_fornecedores')
   # def _selecao_contato(self):
   #    for record in self:
   #       if record.contato_fornecedores:
   #          for contato in record.contato_fornecedores:
   #             if(contato.name == record.escolha_de_contato.value):
   #                record.email_contato_fornecedores = record.contato_fornecedores.email
   #                record.telefone_contato_fornecedores = record.contato_fornecedores.phone
   #                record.celular_contato_fornecedores = record.contato_fornecedores.mobile
                  


        