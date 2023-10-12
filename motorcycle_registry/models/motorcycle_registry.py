from odoo import api, fields, models

class motorcycle_registry(models.Model):
    _name ="motorcycle.registry"
    _description ="Motorcycle Registry"
    _rec_name = "registry_number"
    
    certificate_title = fields.Binary(string="Certificate Title")
    current_mileage = fields.Float(string="Current Mileage")
    date_registry = fields.Date(string="Date Registry")
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    license_plate = fields.Char(string="License Plate") 
    registry_number = fields.Char(string="Registry Number", required=True)    
    vehicle_image = fields.Image(string="Vehicle Image")
    vin = fields.Char(string="Vin", required=True)
    
# TASK-5
    # Create one record from the Motorcycle Registry Model. This Registry should have more than 1000 miles and no license plate.
        # env['motorcycle.registry'].create({'current_mileage': 1200, 'first_name': 'Jim', 'last_name': 'Smith', 'registry_number': 'D123', 'vin': 'vin4', 'license_plate': False})
    
    # Search for all Motorcycles Registries with less than 1000 miles
        # env['motorcycle.registry'].search_read([('current_mileage', '<','1000')])
    
    # Search for all Motorcycle Registries with a VIN but no license plate. Only show the fields: registry_number, vin, license_plate, and lastname
        # env['motorcycle.registry'].search_read([('vin', '!=', False), ('license_plate', '=', False)]),[('registry_number', 'vin', 'license_plate', 'last_name')]      
          
    # Search for all Motorcycle Registries with a date_registry or a VIN
        # env['motorcycle.registry'].search_read(['|', ('date_registry', '!=', False), ('vin', '!=', False)])
    
    # Update the name and last name of the record you created to Francesco Bagnaia
        # env['motorcycle.registry'].search([('id', '=', '1')]).write({'first_name' : 'Francesco', 'last_name' : 'Bagnaia'})
        
    # Delete the record
        # env['motorcycle.registry'].search([('id', '=', '1')]).unlink()