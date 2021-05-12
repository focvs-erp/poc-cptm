# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PlanoContaSecundaria(models.Model):
    _name = 'account.plano_conta_secundaria'
    _description = 'Plano de Conta Secundária'

    codigo = fields.Char(string="Código")
    nome_cta = fields.Char(string="Nome da Conta")
    tipo = fields.Char(string="Conta Superior")
    nivel = fields.Char(string="Nível")
    natureza = fields.Char(string="Natureza")