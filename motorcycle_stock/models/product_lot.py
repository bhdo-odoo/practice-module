from odoo import api, fields, models

class StockLotInherit(models.Model):
    _inherit = 'stock.lot'

    name = fields.Char(compute='_compute_name_lot', store=True, readonly=False)

    @api.depends('product_id.product_tmpl_id.detailed_type', 'product_id.product_tmpl_id.year', 
                'product_id.product_tmpl_id.make', 'product_id.product_tmpl_id.model', 'product_id.product_tmpl_id.battery_capacity', 'name')
    def _compute_name_lot(self):
        for lot in self:
            if lot.product_id.product_tmpl_id.detailed_type == 'motorcycle':
                name_parts = [part for part in [lot.product_id.product_tmpl_id.year, lot.product_id.product_tmpl_id.make, 
                                                lot.product_id.product_tmpl_id.model, lot.product_id.product_tmpl_id.battery_capacity] if part]
                lot.name = ''.join(name_parts)
            else:
                lot.name = lot.name