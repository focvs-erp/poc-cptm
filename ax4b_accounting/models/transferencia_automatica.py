# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TransferenciaAutomatica(models.Model):
    _inherit = "account.transfer.model"
    
    date_stop = fields.Date(string="Data Validade")
    percent = fields.Date(string="Percentual")
    centro_custo_related = fields.Many2one('x_centro_de_custo', string='Centro de Custo')