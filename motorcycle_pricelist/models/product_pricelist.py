from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _inherit = 'motorcycle.registry'
    _inherit = 'sale'

    is_new_customer = fields.Boolean(string="Is New Customer", compute='_compute_is_new_customer')

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.depends('owner_id')
    def _compute_is_new_customer(self):
        for order in self:
            order.partner_id.is_new_customer = not order.env['sale.order'].search([
                ('partner_id', '=', order.partner_id.id),
                ('state', '=', 'sale'),
                ('order_line.product_id.type', '=', 'product'),
                ('order_line.product_id.product_tmpl_id.type', '=', 'motorcycle'),
            ])

    def action_apply_discount(self):
        self.ensure_one()
        # Retrieve the product pricelist with the $2500 discount
        discount_pricelist = self.env.ref('your_module.discount_pricelist_id')
        self.write({'pricelist_id': discount_pricelist.id})
