# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fornecedor(models.Model):
    _inherit = 'account.move	'

    checkbox_bloqueio = fields.Boolean(related='partner_id.bloquear_cadastro', string='Bloqueio de Cadastro', invisible="1")
    payment_reference = fields.Char(String="TESTE")

    @api.depends('checkbox_bloqueio')
    def _total(self):
        if self.checkbox_bloqueio == True:
            self.payment_reference = "TRUE"
        else:
            self.payment_reference = "FALSE"


