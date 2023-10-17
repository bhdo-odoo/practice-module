{
    "name": "Motorcycle Website",
    'summary' : 'Management of Motorcycle Website',
    'description' : '''
        Motorcycle Website Management
        ====================
        This Module is used to keep track of the Motorcycle Management of each brand.
    ''',
    'author' : 'bhdo-odoo',
    'version' : '0.0.1',
    'category' : 'Kawiil/Custom Modules',
    'website' : 'https://github.com/kro-odoo/batch10-practice-module/tree/16.0-motorcycle-registry-bhdo',
    
    "depends": ["motorcycle_stock", "website"],
    "application": True,
    "auto_install": True,
    "installable": True,
    'license': 'LGPL-3',
    "data": [
        'views/motorcycle_compare.xml',
    ],
}
