# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GrupoPatrimonio(models.Model):
    _name = 'account.grupo_patrimonio'
    _description = 'account.grupo_patrimonio'
    
    codigo = fields.Char(string = "Código")
    nome_grupo = fields.Char(string = "Nome do Grupo")
    empresa = fields.Many2one("res.company", string = "Empresa")