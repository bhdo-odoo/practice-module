from odoo import http
from odoo.http import request

class MotorcycleCompareController(http.Controller):

    @http.route('/compare', type='http', auth="public", website=True)
    def compare_page(self, **kw):
        motorcycle_templates = request.env['product.template'].sudo().search([('detailed_type', '=', 'motorcycle')])
        values = {'motorcycle_templates': motorcycle_templates}
        return request.render('motorcycle_website.compare_page_template', values)