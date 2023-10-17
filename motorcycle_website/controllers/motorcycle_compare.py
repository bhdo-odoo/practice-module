from odoo import http
from odoo.http import request

class MotorcycleCompareController(http.Controller):

    @http.route('/compare', auth='public', website=True)
    def motorcycle_compare(self, **kw):
        motorcycles = request.env['product.template'].search([('type', '=', 'motorcycle')])
        return http.request.render('motorcycle_website.motorcycle_compare_template', {
            'motorcycles': motorcycles,
        })
