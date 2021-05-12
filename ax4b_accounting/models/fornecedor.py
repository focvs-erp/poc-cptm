# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fornecedor(models.Model):
    _inherit = 'res.partner'

    # bool_bloquear_cadastro = fields.Boolean(string="Bloquear Cadastro", default=False)

