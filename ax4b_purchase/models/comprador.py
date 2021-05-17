# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Comprador(models.Model):
    _name = 'purchase.comprador'
    _description = 'Cadastro de Comprador'
    
    name = fields.Char(string='Nome Comprador')
    cd_telefone = fields.Char(string='Telefone')
    cd_email = fields.Char(string='Email')
    cd_celular = fields.Char(string='Celular')

    