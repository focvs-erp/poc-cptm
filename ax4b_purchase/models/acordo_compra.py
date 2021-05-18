# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class AcordoDeCompra(models.Model):
    _inherit = 'purchase.requisition'

    situacao_bloqueio = fields.Selection(related='vendor_id.situacao_bloqueio', invisible=1)

    @api.onchange('vendor_id')
    def _fornecedor_bloqueado(self):
        for record in self:
            if record.situacao_bloqueio == '2':
                raise ValidationError("Fornecedor bloqueado para transações")
