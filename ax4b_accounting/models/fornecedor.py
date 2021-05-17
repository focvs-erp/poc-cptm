# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class Fornecedor(models.Model):
    _inherit = 'res.partner'

    situacao = fields.Selection([('1', 'Ativo'), ('2', 'Bloqueado')], required=False, default='1', readonly=True)

    def btn_desbloquear(self):
        self.situacao = '1'
    
    def btn_bloquear(self):
        self.situacao = '2'
        
        
#         message_id = self.env['res.fornecedor_bloqueado_wizard'].create({'message': 'Osam gerados com Sucesso!'})
#         return {
#             'name': 'Mensagem',
#             'res_model': 'res.fornecedor_bloqueado_wizard',
#             'res_id': message_id.id,
#             'view_mode': 'form',
#             'context': {
#                 'active_model': 'res.partner',
#                 'active_ids': self.ids,
#             },
#             'target': 'new',
#             'type': 'ir.actions.act_window',
#         }    
    
#     @api.onchange("bloquear_cadastro")    
#     def _fatura_do_fornecedor(self):  
#         if self.name == False:
#             return 
                
#         if self.bloquear_cadastro == True and len(self.ids) > 0:
#             domain = [('partner_id', '=', self.ids[0])]
#             searched_users = self.env['account.move'].search(domain)
#             if len(searched_users) > 0:
#                 EXIBIR FORM DE CONFIRMAÇÃO
#         return


class FornecedorBloqueadoWizard(models.TransientModel):
    _name = 'res.fornecedor_bloqueado_wizard'
    _description = "Mensagem de Confirmação do Fornecedor Bloqueado"

    message = fields.Text('Confirmação', required=True)
    def yes(self):
        # raise ValidationError(self.env.context.get('active_model'))
        return False

    def no(self):
        return False