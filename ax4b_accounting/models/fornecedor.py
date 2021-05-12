# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fornecedor(models.Model):
    _inherit = 'res.partner'

    bloquear_cadastro = fields.Boolean(string="Bloquear Cadastro")

