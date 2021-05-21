from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class DepreciacaoSocietaria(models.Model):
    _name = 'account.depreciacao_societaria'
    _description = 'Depreciação Societária'

    name = fields.Char(string='Entrada de Diário', copy=False)

    asset = fields.Many2one('account.asset', string='Asset', invisible=True)
    currency_id = fields.Many2one('res.currency', invisible=True, string='Currency', default=lambda self: self.env.company.currency_id.id)

    ref_societaria = fields.Char(string="Referência", copy=False)
    date_societaria = fields.Date(string='Data de Depreciação', copy=False)
    amount_total_societaria = fields.Monetary(string='Depreciação', copy=False)
    asset_depreciated_value_societaria = fields.Monetary(string='Drepreciação Cumulativa', copy=False)
    asset_remaining_value_societaria = fields.Monetary(string='Depreciable Value', copy=False)

    @api.model
    def _preparar_depreciacao_societaria_para_asset(self, vals):
        missing_fields = set(['asset_id', 'move_ref', 'amount', 'asset_remaining_value', 'asset_depreciated_value']) - set(vals)
        if missing_fields:
            raise UserError(_('Está faltando os seguintes campos: {}').format(', '.join(missing_fields)))
        asset = vals['asset_id']
        current_currency = asset.currency_id
        depreciation_date = vals.get('date', fields.Date.context_today(self))
        # amount = current_currency._convert(vals['amount'], asset.company_id.currency_id, asset.company_id, depreciation_date)
        amount = 500
        raise UserError(amount)
        move_vals = {
            'ref_societaria': vals['move_ref'],
            'date_societaria': depreciation_date,
            'asset': asset.id,
            'asset_remaining_value_societaria': vals['asset_remaining_value'],
            'asset_depreciated_value_societaria': vals['asset_depreciated_value'],
            'amount_total_societaria': amount,
            'name': '/',
            # 'asset_value_change': vals.get('asset_value_change', False),
            'currency_id': current_currency.id,
        }
        return move_vals