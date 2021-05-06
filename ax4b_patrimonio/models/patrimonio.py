# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Patrimonio(models.Model):
    _inherit = 'account.asset'

    # Cabeçalho
    numero = fields.Char('Número', readonly=True) # Número sequencial
    data_cri = fields.Date(string = 'Data de Criação')
    num_fis = fields.Char(string = 'Número Físico')
    num_cont = fields.Char(string='Contrato')
    num_nf = fields.Char(string='Nota Fiscal')
    data_docto = fields.Date(string = 'Data do Documento')
    cod_forn = fields.Char(string='Fornecedor')
    
#     Estão comentados devido as relações de models criadas pelo studio, com isso elas ficam salvas no BD e não são acessíveis por D
#     centro_custo_related = fields.Many2one('x_centro_de_custo', string='Centro de Custo')
#     desc_centro_custo_related = fields.Char(related='centro_custo_related.x_studio_descrio', string='Descrição')
    
    # Localização
    desc_loc_localizacao = fields.Char(string='Localização')
    nome_resp_localizacao = fields.Char(string='Resposável')
    desc_dep_localizacao = fields.Char(string='Financeiro')
    num_gis_localizacao = fields.Char(string='Número GIS')
    contato_localizacao = fields.Char(string='Contato')
    desc_obs_localizacao = fields.Char(string='Observação')

    # Dados de seguro
    cod_forn_dados_seguro = fields.Char(string='Fornecedor Seguro')
    nome_agt_dados_seguro = fields.Char(string='Agente')
    num_apol_dados_seguro = fields.Char(string='Número Apólice')
    data_vde_dados_seguro = fields.Date(string='Vigência de')
    data_vate_dados_seguro = fields.Date(string='Vigência até')
    vlr_seg_dados_seguro = fields.Char(string='Valor Segurado')
    vlr_frq_dados_seguro = fields.Char(string='Franquia')
    desc_obs_dados_seguro = fields.Char(string='Observação')
    
    # Dados de garantia
    nome_marca_dados_garantia = fields.Char(string='Marca')
    desc_mod_dados_garantia = fields.Char(string='Ano/Modelo')
    num_serie_dados_garantia = fields.Char(string='Número de Série')
    data_vcto_dados_garantia = fields.Date(string='Vencimento')
    desc_obs_dados_garantia = fields.Char(string='Observações')
    
    # Informações adicionais
    qtd_info_add = fields.Char(string='Quantidade')
    vlr_unit_info_add = fields.Monetary(string='Valor Unitário')
    vlr_tot_info_add = fields.Monetary(string='Valor Total')
    num_atpai_info_add = fields.Char(string='Número Ativo Pai')
    metodo_info_add = fields.Selection([ ('1', 'Straight Line'),('2', 'Declining'),('3', 'Declining then Straight Line')],'Type', default='1')
    metodo_depreciado_info_add = fields.Float(string='Fator de Declínio', default=0.30)
    method_number_info_add = fields.Integer(string='', default = 5)
    method_period_info_add = fields.Selection([('1', 'Month'),('2', 'Year')],'Type', default='1')
    
#     duracao_info_add = fields.Float(string='Duração')
    tipo_tempo_info_add = fields.Char(string='Tempo')
    cod_forn_info_add = fields.Boolean(string='Pro Rata Temporis')
    cod_ccus_info_add = fields.Date(string='Início da Depreciação')

    #Orçamento
    Tabela_Dotacao_orcamento = fields.Many2one('account.journal', string = "Dotação Orçamentária")
    # nome_poder_orcamento = fields.Char(related='Tabela_Dotacao_orcamento.x_studio_many2one_field_4XDnU', string="Poder")
    # cod_poder_orcamento = fields.Char(related='Tabela_Dotacao_orcamento.x_studio_cdigo_do_poder', string="Poder")
    # nome_orgao_orcamento = fields.Char(related='Tabela_Dotacao_orcamento.x_studio_many2one_field_TbDWz', string="Poder")
    # cod_orgao_orcamento = fields.Char(related='Tabela_Dotacao_orcamento.x_studio_cd_orgao', string="Poder")
   
    
    # Campos já existentes dentro do asset, apenas usados para edição de nomes
    original_value = fields.Monetary(string = "Valor de Aquisição")
    salvage_value = fields.Monetary(string = "Valores Não Depreciáveis")
    value_residual = fields.Monetary(string = "Valor Depreciável")
    book_value = fields.Monetary(string = "Valor Residual")
    account_asset_id = fields.Many2one(string = "Conta Aquisição do Ativo")
    first_depreciation_date = fields.Date(string = "Início da Depreciação")


    

