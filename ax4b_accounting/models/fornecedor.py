# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fornecedor(models.Model):
    _inherit = 'res.partner'

    bloqueo_cadastro = fields.Boolean(string='Bloqueo Cadastro', default=False)

