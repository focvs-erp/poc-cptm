# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pagamento(models.Model):
    _inherit = 'account.payment'

    # partner_id = fields.Many2one('partner_id', string="Fornecedor")
    # checkbox_bloqueio = fields.Boolean(related='partner_id.bloquear_cadastro', compute="_bloqueio")
    # ref = fields.Char(string="teste")

    # @api.depends('checkbox_bloqueio')
    # def _bloqueio(self):
    #     for record in self:
    #         if record.checkbox_bloqueio == True:
    #             record.ref = "TRUE"
    #         else:
    #             record.ref = "FALSE"


