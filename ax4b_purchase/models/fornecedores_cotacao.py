from odoo import  models, fields, api

class FornecedoresDaCotacao(models.Model):
   _name = 'purchase.fornecedores_cotacao'
   _description = 'Fornecedores da Cotação'

   name = fields.Char() 
   prioridade = fields.Selection([('0', 'Normal'), ('1', 'Urgent')], 'Priority', default='0', index=True)
   cotacao_de_compra = fields.Many2one("purchase.cotacao_compra", invisible=True, string="Cotação de Compra")
   fornecedores = fields.Many2one("res.partner", string="Fornecedores")
   nome_contato = fields.Char()
   contato_fornecedores = fields.One2many(related="fornecedores.child_ids", string="Contato")
  
   # escolha_de_contato = fields.Selection([('', 'record.contato_fornecedores.name'), ['4','Sem registros']],compute='_contato_fornecedores', store= True)
   #contact = fields.Char(related="vendors.name")
   # telefone_contato_fornecedores = fields.Char(compute='_selecao_contato', store=True)
   # celular_contato_fornecedores = fields.Char(compute='_selecao_contato', store=True)
   # selecao_contato = fields.Char(compute='_selecao_contato', store=True)
   #nome_fornecedor = fields.Char(related="fornecedores.name")

   teste = fields.Selection([], string="Contato Fornecedor")
   email_contato_fornecedores = fields.Char(compute='_onchange_fornecedore', store=True)
   email = fields.Char(related="fornecedores.email", string="Email")
   telefone = fields.Char(related="fornecedores.phone", string="Telefone") 
   celular = fields.Char(related="fornecedores.mobile", string="Celular") 
  
   
   
   @api.onchange('fornecedores')
   def _onchange_fornecedore(self):
      contato_array= []
      for record in self:
          if record.contato_fornecedores:
             for contato in record.contato_fornecedores:
               contato_array.append((str(contato.name), str(contato.name)))
               
      return {'domain' : 
             {'teste':
             [contato_array] }}

   # @api.depends('fornecedores')
   # def _add_contato(self):
   #    return [('1', 'option1'), ('2', 'option2')]


   # @api.depends('fornecedores')
   # def _selecao_contato(self):
   #    for record in self:
   #       if record.contato_fornecedores:
   #          for contato in record.contato_fornecedores:
   #             listEmail = [('1',"Rafael teste ")]
   #             # if(contato.name == record.escolha_de_contato.value):
   #             record.email_contato_fornecedores = "Rafael"
   #             record.teste = listEmail
   #             # record.telefone_contato_fornecedores = record.contato_fornecedores.phone
   #             # record.celular_contato_fornecedores = record.contato_fornecedores.mobile
                  

   # @api.depends('fornecedores')
   # def _add_contato(self):
   #    list1 = []
   #    list1.append(('1', 'option1'))
   #    if self.contato_fornecedores:
   #       list1.append((str('3', 'option32')))

         # for contato in record.contato_fornecedores:
            # list1.append((str(contato.name), str(contato.name)))
      # self.teste = list1            
      # return list1
        
   
   # @api.depends('fornecedores')
   # def _add_contato(self):
   #    contato_array= []
      
   #    return [('1', 'option1'), ('2', 'option2')]