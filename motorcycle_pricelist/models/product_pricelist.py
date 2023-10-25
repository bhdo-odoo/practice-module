from odoo import models, fields, api

class SalesInherit(models.Model):
    _inherit = "sale.order"
    is_new_customer = fields.Boolean(compute="_compute_is_new_customer")

    @api.depends('partner_id')
    def _compute_is_new_customer(self):
        self.is_new_customer = True
        if self.partner_id :
            partner = self.env['res.partner'].search([('id','=',self.partner_id.id)])
            partner_sale_orders = partner[0].sale_order_ids
            self.is_new_customer = True 
            for order in partner_sale_orders:
                if not self.env['product.template'].search([('detailed_type','=','product'),('id','=',order.id)]):
                    self.is_new_customer = False
                    break

    def action_new_customer(self):
        first_time_buyer_pricelist = self.env.ref('motorcycle_pricelist.pricelist_first_time_buyer')
        self.pricelist_id = first_time_buyer_pricelist
        self.action_update_prices()
        self.is_new_customer = False