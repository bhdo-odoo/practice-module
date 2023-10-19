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
    battery_capacity = fields.Selection([('xs', 'Small'), ('0m', 'Medium'), ('0l', 'Long'), ('xl', 'Extra Large')], string='Battery Capacity')
    charge_time = fields.Float(string='Charge Time')
    range = fields.Float(string='Range')
    curb_weight = fields.Float(string='Curb Weight')
    make = fields.Char(string='Make')
    model = fields.Char(string='Model')
    year = fields.Char(string='Year')
    launch_date = fields.Date(string='Launch Date')

    @api.model
    def create(self, values):
        if values.get('type') == 'product' and values.get('product_variant_count', 0) == 1:
            product_variant = self.env['product.product'].create({
                'year': values.get('year'),
                'make': values.get('make'),
                'model': values.get('model'),
                'detailed_type': values.get('detailed_type'),
            })
            if product_variant.detailed_type == 'motorcycle':
                values['name'] = f"{product_variant.year} {product_variant.make} {product_variant.model}"

        product_template = super(ProductTemplateInherit, self).create(values)

        return product_template



    # @api.depends('name', 'make', 'model', 'year', 'detailed_type')
    # def _compute_motorcycle_name(self):
    #     for template in self: 
    #         if template.type == 'product' and template.product_variant_count == 1:
    #             variant = template.product_variant_ids
    #             if variant.detailed_type == 'motorcycle':
    #                 template.name = f"{variant.year}{variant.make}{variant.model}"
    #             else:
    #                 template.name = template.name
    #         else:
    #             template.name = template.name
        # for template in self:
        #     variant = template.product_variant_ids
        #     if variant.detailed_type != 'motorcycle':
        #         return variant.name
        #     elif variant.detailed_type == 'motorcycle':
        #             template.name = f"{variant.make}{variant.model}{variant.year}"
        #     else:
        #         template.name = ""
