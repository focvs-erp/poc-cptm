from odoo import models, fields, api

class DepreciacaoSocietaria(models.Model):
    _name = 'account.depreciacao_societaria'
    _description = 'Depreciação Societária'

    # asset_id_societaria = fields.Many2one('account.asset', string='Asset', index=True, ondelete='cascade', copy=False, domain="[('company_id', '=', company_id)]")
    asset_id_societaria = fields.Many2one('account.asset', string='Asset')
    asset_asset_type_societaria = fields.Selection(related='asset_id_societaria.asset_type')
    # asset_remaining_value_societaria = fields.Monetary(string='Depreciable Value', copy=False)
    # asset_depreciated_value_societaria = fields.Monetary(string='Cumulative Drepreciation', copy=False)
    # asset_value_change_societaria = fields.Boolean(help='This is a technical field set to true when this move is the result of the changing of value of an asset')