# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CadastroComprador(models.Model):
    _name = 'purchase.cadastro_comprador'
    _description = 'Cadastro de Comprador'
    
    nome_comprador = fields.Char(string='Nome Comprador')
    cd_telefone = fields.Char(string='Telefone')
    cd_email = fields.Char(string='Email')
    cd_celular = fields.Char(string='Celular')

    