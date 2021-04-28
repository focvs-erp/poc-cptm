# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cptm_custom(models.Model):
    _name = 'cptm_custom.cptm_custom'
    _description = 'cptm_custom.cptm_custom'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    numero_requicao = fields.Text(string = "Número da Requisição")
    teste = fields.Text(string = "Teste push")

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
