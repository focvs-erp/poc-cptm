# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PlanoContaAX4B(models.Model):
    _inherit = 'account.account'

    cod_red = fields.Char(string="Código Reduzido")

    cod_refrfb = fields.Many2one(
        'account.plano_referencial',
        string="Conta Referencial RFB")

    cod_ctacons = fields.Char(string="Conta Consolidação")

    cod_ctasec = fields.Many2one(
        'account.plano_conta_secundaria',
        string="Conta Referencial Secundária")

    manual = fields.Boolean(string="Não Permitir Entrada Manual")

    cod_ctapai = fields.Char(string="Conta Pai")

    cod_catpri = fields.Char(string="Categoria de Conta Principal")

    centro_custo_related = fields.Many2one('x_centro_de_custo', string='Centro de Custo')

    padrao = fields.Selection(
        [("1", "Débito"),
         ("2", "Crédito")],
        string="Padrão DB/CR")

    nece_dc = fields.Selection(
        [("1", "Débito"),
         ("2", "Crédito")],
        string="Necessidade DB/CR")
