{
    'name' : 'Motorcycle Registry',
    'summary' : 'Manage Registration of Motorcycles',
    'description' : '''
        Motorcycle Registry
        ====================
        This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycle of the brand.
    ''',
    'author' : 'bhdo-odoo',
    'version' : '0.0.1',
    'category' : 'Kawiil/Custom Modules',
    'website' : 'https://github.com/kro-odoo/batch10-practice-module/tree/16.0-motorcycle-registry-bhdo',
    "demo": [
        'demo/demo_data.xml',
    ],
    "data": [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/motorcycle_registry_views.xml',
        'data/motorcycle_registry_data.xml',
        'views/motorcycle_registry_menus.xml',
    ],
    'application' : True,
    'installable' : True,
    'license' : 'LGPL-3'
}