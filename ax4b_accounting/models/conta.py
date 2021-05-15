# -*- coding: utf-8 -*-

# from odoo import models, fields, api
# from odoo.exceptions import UserError, ValidationError

# class Conta(models.Model):
#     _inherit = 'account.move'

#     situacao_fornecedor = fields.Selection(related='partner_id.situacao', invisible=1)

#     @api.onchange('partner_id')
#     def _fornecedor_bloqueado(self):
#         for record in self:
#             if record.situacao_fornecedor == '2':
#                 raise ValidationError("Fornecedor bloqueado para transações")

#     def action_register_payment(self):
#         if self.situacao_fornecedor == '2':
#             raise ValidationError("Fornecedor bloqueado para transações")

#         res = super(Conta, self).action_register_payment()
#         return res