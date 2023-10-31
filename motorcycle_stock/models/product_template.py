from odoo import models, fields, api

class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    detailed_type = fields.Selection(selection_add=[('motorcycle', 'Motorcycle')], ondelete={'motorcycle': 'set product'})
    
    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['motorcycle'] = 'product'
        return type_mapping

    horsepower = fields.Float(string='Horsepower')
    top_speed = fields.Float(string='Top Speed')
    torque = fields.Float(string='Torque')
    battery_capacity = fields.Selection([('xs', 'Small'), ('0m', 'Medium'), ('0l', 'Large'), ('xl', 'Extra Large')], 
                                        string='Battery Capacity')
    charge_time = fields.Float(string='Charge Time')
    range = fields.Float(string='Range')
    curb_weight = fields.Float(string='Curb Weight')
    make = fields.Char(string='Make')
    model = fields.Char(string='Model')
    year = fields.Char(string='Year')
    launch_date = fields.Date(string='Launch Date')

    name = fields.Char(compute='_compute_name_product', store=True, readonly=False)

    @api.depends('detailed_type', 'make', 'model', 'year')
    def _compute_name_product(self):
        for product in self:
            if product.detailed_type == 'motorcycle':
                name_parts = [part for part in [product.year, product.make, product.model] if part]
                product.name = ' '.join(name_parts)
            else:
                product.name = super(ProductTemplateInherit, product).name