# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ax4b_patrimonio(models.Model):
#     _name = 'ax4b_patrimonio.ax4b_patrimonio'
#     _description = 'ax4b_patrimonio.ax4b_patrimonio'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
