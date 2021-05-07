# -*- coding: utf-8 -*-

from odoo import models, fields, api

class FornecedorDoPatrimonio(models.Model):
    _name = 'account.fornecedor_patrimonio'
    _description = 'Tabela de Fornecedor'

    # Dados de seguro
#     patrimonio = fields.Many2one('ax4b_patrimonio.patrimonio')
    cod_forn_dados_seguro = fields.Many2one('res.partner', string='Fornecedor')
    nome_agt_dados_seguro = fields.Char(string='Agente')
    num_apol_dados_seguro = fields.Char(string='Número Apólice')
    data_vde_dados_seguro = fields.Date(string='Vigência de')
    data_vate_dados_seguro = fields.Date(string='Vigência até')
    vlr_seg_dados_seguro = fields.Char(string='Valor Segurado')
    vlr_frq_dados_seguro = fields.Char(string='Franquia')
    desc_obs_dados_seguro = fields.Char(string='Observação')
    

