# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.tools import float_compare, float_is_zero, float_round
import calendar
from math import copysign
from odoo.exceptions import UserError, ValidationError

class Patrimonio(models.Model):
    _inherit = 'account.asset'

    # Cabeçalho
    name = fields.Char(string='Número', default='PAT_00000000') # Número sequencial
    data_cri = fields.Date(string = 'Data de Criação', default=lambda self: fields.Date.today())
    num_fis = fields.Char(string = 'Número Físico')
    num_cont = fields.Char(string='Contrato')
    num_nf = fields.Char(string='Nota Fiscal')
    data_docto = fields.Date(string = 'Data do Documento')
    cod_forn = fields.Char(string='Fornecedor')
    centro_custo_related = fields.Many2one('x_centro_de_custo', string='Centro de Custo')
    desc_centro_custo_related = fields.Char(related='centro_custo_related.x_studio_descrio', string='Descrição')
    
    # Localização
    desc_loc_localizacao = fields.Char(string='Localização')
    nome_resp_localizacao = fields.Char(string='Resposável')
    desc_dep_localizacao = fields.Char(string='Financeiro')
    num_gis_localizacao = fields.Char(string='Número GIS')
    contato_localizacao = fields.Char(string='Contato')
    desc_obs_localizacao = fields.Char(string='Observação')

    # Dados de seguro
#     cod_forn_dados_seguro = fields.Char(string='Fornecedor Seguro')
#     cod_forn_dados_seguro = fields.Many2one('account.forncedores_patrimonio')
    nome_agt_dados_seguro = fields.Char(string='Agente')
    num_apol_dados_seguro = fields.Char(string='Número Apólice')
    data_vde_dados_seguro = fields.Date(string='Vigência de')
    data_vate_dados_seguro = fields.Date(string='Vigência até')
    vlr_seg_dados_seguro = fields.Char(string='Valor Segurado')
    vlr_frq_dados_seguro = fields.Char(string='Franquia')
    desc_obs_dados_seguro = fields.Char(string='Observação')
    table_dados_seguro = fields.One2many('account.seguro_patrimonio', 'patrimonio',string='Fornecedor Seguro')
    
    # Dados de garantia
    nome_marca_dados_garantia = fields.Char(string='Marca')
    desc_mod_dados_garantia = fields.Char(string='Ano/Modelo')
    num_serie_dados_garantia = fields.Char(string='Número de Série')
    data_vcto_dados_garantia = fields.Date(string='Vencimento')
    desc_obs_dados_garantia = fields.Char(string='Observações')

    # Depreciação Societária
    depreciation_move_ids_societaria = fields.One2many('account.depreciacao_societaria', 'asset', string='Depreciation Lines')
   
    
    # Informações adicionais Page
    qtd_info_add = fields.Integer(string='Quantidade')
    vlr_unit_info_add = fields.Monetary(string='Valor Unitário')
    vlr_tot_info_add = fields.Monetary(string='Valor Total', compute='_total')
    num_atpai_info_add = fields.Many2one('account.asset', string='Número Ativo Pai')


    # Informações adicionais
    metodo_info_add = fields.Selection([('1', 'Straight Line'),('2', 'Declining'),('3', 'Declining then Straight Line')],'Método', default='1')
    metodo_depreciado_info_add = fields.Float(string='Fator de Declínio', default=0.30)
    cod_forn_info_add = fields.Boolean()
    cod_forn_date_info_add = fields.Date(string='Prorata Date', default=lambda self: fields.Date.today())
    cod_ccus_info_add = fields.Date(string='Início da Depreciação', compute='_compute_first_depreciation_date_societaria',) 
    method_number_info_add = fields.Integer(string='', default = 5)
    method_period_info_add = fields.Selection([('1', 'Month'),('12', 'Year')],'Type', default='1')
    
    # duracao_info_add = fields.Float(string='Duração')
    tipo_tempo_info_add = fields.Char(string='Tempo')
    
    # Orçamento
    tabela_dotacao_orcamento = fields.Many2one('x_dotacao', string = "Dotação Orçamentária")
    nome_poder_orcamento = fields.Many2one(related='tabela_dotacao_orcamento.x_studio_many2one_field_4XDnU', string="Poder")
    cod_poder_orcamento = fields.Char(related='tabela_dotacao_orcamento.x_studio_cdigo_do_poder', string="Código do Poder")
    nome_orgao_orcamento = fields.Many2one(related='tabela_dotacao_orcamento.x_studio_many2one_field_TbDWz', string="Órgão")
    cod_orgao_orcamento = fields.Char(related='tabela_dotacao_orcamento.x_studio_cd_orgao', string="Código do Órgão")
    nome_unidade_orcamento = fields.Many2one(related='tabela_dotacao_orcamento.x_studio_ds_uo', string="Unidade Orçamentária")
    cod_unidade_orcamento = fields.Char(related='tabela_dotacao_orcamento.x_studio_ds_uo.x_studio_cdigo', string="Código da Unidade Orçamentária")
    grupo_unidade_orcamento = fields.Many2one(related='tabela_dotacao_orcamento.x_studio_ds_grupo', string='Grupo')
    cod_grupo_unidade_orcamento = fields.Char(related='tabela_dotacao_orcamento.x_studio_cd_grupo', string='Código do Grupo')
    funcao_unidade_orcamento = fields.Many2one(related='tabela_dotacao_orcamento.x_studio_ds_funcao', string='Função')
    cod_funcao_unidade_orcamento = fields.Char(related='tabela_dotacao_orcamento.x_studio_cd_funcao', string='Código da Função')
    programas_unidade_orcamento = fields.Many2one(related='tabela_dotacao_orcamento.x_studio_ds_programa', string='Programas')
    cod_programas_unidade_orcamento = fields.Char(related='tabela_dotacao_orcamento.x_studio_cod_programa', string='Código do Programa')
    fonte_unidade_orcamento = fields.Many2one(related='tabela_dotacao_orcamento.x_studio_ds_fontes', string='Fontes')
    cod_fonte_unidade_orcamento = fields.Char(related='tabela_dotacao_orcamento.x_studio_cod_fonte', string='Código da Fonte')
    categoria_unidade_orcamento = fields.Many2one(related='tabela_dotacao_orcamento.x_studio_ds_categoria', string='Categoria')
    cod_categoria_unidade_orcamento = fields.Char(related='tabela_dotacao_orcamento.x_studio_cd_categoria', string='Código da Categoria')
    classe_unidade_orcamento = fields.Many2one(related='tabela_dotacao_orcamento.x_studio_many2one_field_q9JSY', string='Classes')
    cod_classe_unidade_orcamento = fields.Char(related='tabela_dotacao_orcamento.x_studio_cd_classe', string='Código da Classe')
    modalidade_unidade_orcamento = fields.Many2one(related='tabela_dotacao_orcamento.x_studio_ds_modalide', string='Modalidades')
    cod_modalidade_unidade_orcamento = fields.Char(related='tabela_dotacao_orcamento.x_studio_cd_modalidade', string='Código da Modalidade')
    elemento_unidade_orcamento = fields.Many2one(related='tabela_dotacao_orcamento.x_studio_ds_elemento', string='Elemento')
    cod_elemento_unidade_orcamento = fields.Char(related='tabela_dotacao_orcamento.x_studio_cod_elemento', string='Código do Elemento')
    subfuncao_unidade_orcamento = fields.Many2one(related='tabela_dotacao_orcamento.x_studio_ds_subfuncao', string='Sub Função')
    cod_subfuncao_unidade_orcamento = fields.Char(related='tabela_dotacao_orcamento.x_studio_cd_subfuncao', string='Código da SubFunção')
    projeto_atividade_unidade_orcamento = fields.Many2one(related='tabela_dotacao_orcamento.x_studio_ds_projeto_atividade', string='Projeto Atividade')
    cod_projeto_atividade_unidade_orcamento = fields.Char(related='tabela_dotacao_orcamento.x_studio_cd_projeto_atividade', string='Código do Projeto da Atividade')   
    
    # Campos já existentes dentro do asset, apenas usados para edição de nomes
    original_value = fields.Monetary(string = "Valor de Aquisição")
    salvage_value = fields.Monetary(string = "Valores Não Depreciáveis")
    value_residual = fields.Monetary(string = "Valor Depreciável")
    book_value = fields.Monetary(string = "Valor Residual")
    account_asset_id = fields.Many2one(string = "Conta Aquisição do Ativo")
    first_depreciation_date = fields.Date(string = "Início da Depreciação")
    
    # on create method
    @api.model
    def create(self, vals):
        obj = super(Patrimonio, self).create(vals)
        number = self.env['ir.sequence'].get('x_patimonio')
        obj.write({'name': number})
        return obj
    

    @api.depends('qtd_info_add', 'vlr_unit_info_add')
    def _total(self):
        self.vlr_unit_info_add = float(self.vlr_unit_info_add)
        if(self.qtd_info_add > 0.00):
            self.vlr_tot_info_add = self.qtd_info_add * self.vlr_unit_info_add
        else: 
            self.vlr_tot_info_add = 0

    def btn_mudar_status_para_draft(self):
        self.write({'state': 'draft'})


    # MÉTODO VALIDATE CHAMAR A DEPRECIAÇÃO SOCIETÁRIA
    def validate(self):
        result = super(Patrimonio, self).validate()
        if not self.depreciation_move_ids_societaria:
            self.compute_depreciation_societaria()
        return result

    def compute_depreciation_societaria(self):
        # amount_change_ids = self.depreciation_move_ids_societaria.sorted(key=lambda l: l.date_societaria)
        amount_change_ids = []
        posted_depreciation_move_ids = []
        already_depreciated_amount = 0
        depreciation_number = self.method_number_info_add
        if self.cod_forn_info_add:
            depreciation_number += 1
        starting_sequence = 0
        amount_to_depreciate = self.original_value - self.salvage_value
        depreciation_date = self.cod_ccus_info_add
        # if we already have some previous validated entries, starting date is last entry + method period
        if posted_depreciation_move_ids and posted_depreciation_move_ids[-1].date:
            last_depreciation_date = fields.Date.from_string(posted_depreciation_move_ids[-1].date)
            if last_depreciation_date > depreciation_date:  # in case we unpause the asset
                depreciation_date = last_depreciation_date + relativedelta(months=+int(self.method_period_info_add))

        commands = []
        # commands = [(2, line_id.id, False) for line_id in self.depreciation_move_ids_societaria.filtered(lambda x: x.state == 'draft')]
        newlines = []
        newlines = self._recompute_board_societaria(depreciation_number, starting_sequence, amount_to_depreciate, depreciation_date, already_depreciated_amount, amount_change_ids)
        newline_vals_list = []
        for newline_vals in newlines:
            # no need of amount field, as it is computed and we don't want to trigger its inverse function
            # del(newline_vals['amount_total'])
            newline_vals_list.append(newline_vals)
        new_moves = self.env['account.depreciacao_societaria'].create(newline_vals_list)
        for move in new_moves:
            commands.append((4, move.id))
        return self.write({'depreciation_move_ids_societaria': commands})


    def _recompute_board_societaria(self, depreciation_number, starting_sequence, amount_to_depreciate, depreciation_date, already_depreciated_amount, amount_change_ids):
        # self.ensure_one()
        residual_amount = amount_to_depreciate
        # Remove old unposted depreciation lines. We cannot use unlink() with One2many field
        move_vals = []
        prorata = self.cod_forn_info_add and not self.env.context.get("ignore_prorata")
        if amount_to_depreciate != 0.0:
            for asset_sequence in range(starting_sequence + 1, depreciation_number + 1):
                # while amount_change_ids and amount_change_ids[0].date_societaria <= depreciation_date:
                #     if not amount_change_ids[0].reversal_move_id:
                #         residual_amount -= amount_change_ids[0].amount_total
                #         amount_to_depreciate -= amount_change_ids[0].amount_total
                #         already_depreciated_amount += amount_change_ids[0].amount_total
                #     amount_change_ids[0].write({
                #         'asset_remaining_value': float_round(residual_amount, precision_rounding=self.currency_id.rounding),
                #         'asset_depreciated_value': amount_to_depreciate - residual_amount + already_depreciated_amount,
                #     })
                #     amount_change_ids -= amount_change_ids[0]
                amount = self._compute_board_amount_societaria(asset_sequence, residual_amount, amount_to_depreciate, depreciation_number, starting_sequence, depreciation_date)
                prorata_factor = 1
                move_ref = self.name + ' (%s/%s)' % (prorata and asset_sequence - 1 or asset_sequence, self.method_number_info_add)
                if prorata and asset_sequence == 1:
                    move_ref = self.name + ' ' + '(prorata entry)'
                    first_date = self.cod_forn_date_info_add
                    if int(self.method_period_info_add) % 12 != 0:
                        month_days = calendar.monthrange(first_date.year, first_date.month)[1]
                        days = month_days - first_date.day + 1
                        prorata_factor = days / month_days
                    else:
                        total_days = (depreciation_date.year % 4) and 365 or 366
                        days = (self.company_id.compute_fiscalyear_dates(first_date)['date_to'] - first_date).days + 1
                        prorata_factor = days / total_days
                amount = self.currency_id.round(amount * prorata_factor)
                if float_is_zero(amount, precision_rounding=self.currency_id.rounding):
                    continue
                residual_amount -= amount

                move_vals.append(self.env['account.depreciacao_societaria']._preparar_depreciacao_societaria_para_asset({
                    'amount': amount,
                    'asset_id': self,
                    'move_ref': move_ref,
                    'date': depreciation_date,
                    'asset_remaining_value': float_round(residual_amount, precision_rounding=self.currency_id.rounding),
                    'asset_depreciated_value': amount_to_depreciate - residual_amount + already_depreciated_amount,
                }))

                depreciation_date = depreciation_date + relativedelta(months=+int(self.method_period_info_add))
                # datetime doesn't take into account that the number of days is not the same for each month
                if int(self.method_period_info_add) % 12 != 0:
                    max_day_in_month = calendar.monthrange(depreciation_date.year, depreciation_date.month)[1]
                    depreciation_date = depreciation_date.replace(day=max_day_in_month)
        return move_vals


    def _compute_board_amount_societaria(self, computation_sequence, residual_amount, total_amount_to_depr, max_depreciation_nb, starting_sequence, depreciation_date):
        amount = 0
        if computation_sequence == max_depreciation_nb:
            # last depreciation always takes the asset residual amount
            amount = residual_amount
        else:
            if self.metodo_info_add in ('2', '3'):
                amount = residual_amount * self.metodo_depreciado_info_add
            if self.metodo_info_add in ('1', '3'):
                nb_depreciation = max_depreciation_nb - starting_sequence
                #cod_forn_info_add = prorata
                if self.cod_forn_info_add:
                    nb_depreciation -= 1
                linear_amount = min(total_amount_to_depr / nb_depreciation, residual_amount)
                if self.metodo_info_add == '3':
                    amount = max(linear_amount, amount)
                else:
                    amount = linear_amount
        return amount

    @api.depends('acquisition_date', 'original_move_line_ids', 'metodo_info_add', 'company_id')
    def _compute_first_depreciation_date_societaria(self):
        for record in self:
            pre_depreciation_date = record.acquisition_date or min(record.original_move_line_ids.mapped('date'), default=record.acquisition_date) or fields.Date.today()
            depreciation_date = pre_depreciation_date + relativedelta(day=31)
            # ... or fiscalyear depending the number of period
            if record.method_period == '12':
                depreciation_date = depreciation_date + relativedelta(month=int(record.company_id.fiscalyear_last_month))
                depreciation_date = depreciation_date + relativedelta(day=record.company_id.fiscalyear_last_day)
                if depreciation_date < pre_depreciation_date:
                    depreciation_date = depreciation_date + relativedelta(years=1)
            record.first_depreciation_date = depreciation_date