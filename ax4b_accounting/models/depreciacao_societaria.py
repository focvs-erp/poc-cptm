from odoo import models, fields, api


class DepreciacaoSocietaria(models.Model):
    _name = 'account.depreciacao_societaria'
    _description = 'Depreciação Societária'

    name = fields.Char(string='Entrada de Diário', copy=False)

    asset = fields.Many2one('account.asset', string='Asset', invisible=True)
    currency_id = fields.Many2one(related='asset.currency_id', invisible=True)

    ref_societaria = fields.Char(string="Referência", copy=False)
    date_societaria = fields.Date(string='Data de Depreciação', copy=False)
    amount_total_societaria = fields.Monetary(string='Depreciação', copy=False)
    asset_depreciated_value_societaria = fields.Monetary(string='Drepreciação Cumulativa', copy=False)
    asset_remaining_value_societaria = fields.Monetary(string='Depreciable Value', copy=False)
