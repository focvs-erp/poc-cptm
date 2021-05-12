# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fornecedor(models.Model):
    _inherit = 'res.partner'

    active = fields.Boolean(string="Bloquer Cadastro", default=True)

