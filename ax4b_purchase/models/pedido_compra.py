# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class PedidoCompra(models.Model):
    _inherit = 'purchase.order'

    situacao_bloqueio = fields.Selection(related='partner_id.situacao_bloqueio', invisible=1)

    @api.onchange('partner_id')
    def _fornecedor_bloqueado(self):
        for record in self:
            if record.situacao_bloqueio == '2':
                raise ValidationError("Fornecedor bloqueado para transações")
