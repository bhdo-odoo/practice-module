{
    "name": "Motorcycle Stock",
    'summary' : 'Management of Motorcycle Stock',
    'description' : '''
        Motorcycle Stock
        ====================
        This Module is used to keep track of the Motorcycle Stock of each brand.
    ''',
    'author' : 'bhdo-odoo',
    'version' : '0.0.1',
    'category' : 'Kawiil/Custom Modules',
    'website' : 'https://github.com/kro-odoo/batch10-practice-module/tree/16.0-motorcycle-registry-bhdo',
    
    "depends": ["stock", "product"],
    "application": True,
    "auto_install": True,
    "installable": True,
    'license': 'LGPL-3',
    "data": [
        'views/product_template.xml',
    ],
}
