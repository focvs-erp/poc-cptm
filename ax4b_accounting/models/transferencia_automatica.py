# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TransferenciaAutomatica(models.Model):
    _inherit = "account.transfer.model"
    
    date_stop = fields.Date(string="Data Validade")