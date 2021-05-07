# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SeguroDoPatrimonio(models.Model):
    _name = 'account.seguro_patrimonio'
    _description = 'Seguro do Patrimônio'

    # Dados de seguro
    patrimonio = fields.Many2one('account.asset')
    cod_forn_dados_seguro = fields.Many2one('res.partner', string='Fornecedor')
    nome_agt_dados_seguro = fields.Char(string='Agente')
    num_apol_dados_seguro = fields.Char(string='Número Apólice')
    data_vde_dados_seguro = fields.Date(string='Vigência de')
    data_vate_dados_seguro = fields.Date(string='Vigência até')
    vlr_seg_dados_seguro = fields.Float(string='Valor Segurado')
    vlr_frq_dados_seguro = fields.Char(string='Franquia')
    desc_obs_dados_seguro = fields.Char(string='Observação')
    

