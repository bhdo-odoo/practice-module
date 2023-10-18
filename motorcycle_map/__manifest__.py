{
    "name": "Motorcycle Map",
    'summary' : 'Management of Motorcycle Map',
    'description' : '''
        Motorcycle Map Management
        ====================
        This Module is used to keep track of the Motorcycle Management of each brand.
    ''',
    'author' : 'bhdo-odoo',
    'version' : '0.0.1',
    'category' : 'Kawiil/Custom Modules',
    'Map' : 'https://github.com/kro-odoo/batch10-practice-module/tree/16.0-motorcycle-registry-bhdo',
    
    "depends": ['motorcycle_registry','web_map'],
    "application": True,
    "auto_install": True,
    "installable": True,
    'license': 'LGPL-3',
    "data": [
        'views/motorcycle_map_views.xml',
    ],
}
