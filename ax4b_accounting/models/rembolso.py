# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Rembolso(models.Model):
    _inherit = 'account.move'

    partner_id = fields.Many2one(string="Fornecedor")
    checkbox_bloqueio = fields.Boolean(related='partner_id.bloquear_cadastro', compute="_bloqueio")
    payment_reference = fields.Char(string="teste123")

    @api.depends('checkbox_bloqueio')
    def _bloqueio(self):
        for record in self:
            if record.checkbox_bloqueio == True:
                record.payment_reference = "TRUE"
            else:
                record.payment_reference = "FALSE"


