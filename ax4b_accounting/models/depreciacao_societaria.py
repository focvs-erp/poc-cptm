from odoo import models, fields, api

class DepreciacaoSocietaria(models.Model):
    _name = 'account.depreciacao_societaria'
    _description = 'Depreciação Societária'

    
    asset_id_societaria = fields.Many2one('account.asset', string='Asset')
    asset_asset_type_societaria = fields.Selection(related='asset_id_societaria.asset_type')
    asset_remaining_value_societaria = fields.Monetary(string='Depreciable Value', copy=False)
    # asset_depreciated_value_societaria = fields.Monetary(string='Cumulative Drepreciation', copy=False)
    asset_manually_modified_societaria = fields.Boolean(help='This is a technical field stating that a depreciation line has been manually modified. It is used to recompute the depreciation table of an asset/deferred revenue.', copy=False)
    asset_value_change_societaria = fields.Boolean(help='This is a technical field set to true when this move is the result of the changing of value of an asset')

    asset_ids_societaria = fields.One2many('account.asset', string='Assets', compute="_compute_asset_ids")
    asset_ids_display_name_societaria = fields.Char(compute="_compute_asset_ids")  # just a button label. That's to avoid a plethora of different buttons defined in xml
    asset_id_display_name_societaria = fields.Char(compute="_compute_asset_ids")   # just a button label. That's to avoid a plethora of different buttons defined in xml
    number_asset_ids_societaria = fields.Integer(compute="_compute_asset_ids")
    draft_asset_ids_societaria = fields.Boolean(compute="_compute_asset_ids")

    # reversed_entry_id is set on the reversal move but there is no way of knowing is a move has been reversed without this
    reversal_move_id_societaria = fields.One2many('account.move', 'reversed_entry_id')
