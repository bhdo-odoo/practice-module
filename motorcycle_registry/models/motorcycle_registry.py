from odoo import api, fields, models
import re
from odoo.exceptions import UserError

class MotorcycleRegistry(models.Model):
    _name ="motorcycle.registry"
    _description ="Motorcycle Registry"
    _rec_name = "registry_number"

    certificate_title = fields.Binary(string="Certificate Title")
    current_mileage = fields.Float(string="Current Mileage")
    date_registry = fields.Date(string="Date Registry")
    license_plate = fields.Char(string="License Plate") 
    registry_number = fields.Char(string="Registry Number", required=True)
    vehicle_image = fields.Image(string="Vehicle Image")
    vin = fields.Char(string="Vin", required=True)

    _sql_constraints = [('vin_unique', 'UNIQUE(vin)', 'VIN number cannot be same for different vehicles')]

    @api.model
    def create(self, vals):
        vals['registry_number'] = self.env['ir.sequence'].next_by_code('motorcycle.registry.sequence')
        return super(MotorcycleRegistry, self).create(vals)

    @api.constrains('vin')
    def check_valid_vin(self) :
        pattern = '^[A-Z]{4}\d{2}[A-Z0-9]{2}\d{5}$'
        if not re.match(pattern, self.vin) :
            raise UserError("The VIN Number should follow the following Pattern: Make - 2 capital letters, Model - 2 capital letters, Year - 2 digits, Battery Capacity - 2 capital letters or numbers, Serial Number - 5 digits")

    @api.constrains('license_plate')
    def _check_license_plate_pattern(self):
        pattern = '^[A-Z]{1,4}\d{1,3}[A-Z]{0,2}$'
        for record in self:
            license_plate = record.license_plate
            if license_plate:
                if not re.match(pattern, license_plate):
                    raise UserError("Invalid License Plate Number. It should follow the pattern: 1-4 Letters, 1-3 Digits, Optional 2 Letters. Eg: KLV453 or KLR343L")
                
    owner_id = fields.Many2one('res.partner', string="Owner")
    email = fields.Char(string="Email", related="owner_id.email")
    phone = fields.Char(string="Phone", related="owner_id.phone")

    make = fields.Char(string="Make", compute='_compute_make', store=True)
    model = fields.Char(string="Model", compute='_compute_model', store=True)
    year = fields.Char(string="Year", compute='_compute_year', store=True)

    @api.depends('vin')
    def _compute_make(self):
        for record in self:
            vin = record.vin
            if vin:
                record.make = vin[0:2]
            else:
                record.make = ""

    @api.depends('vin')
    def _compute_model(self):
        for record in self:
            vin = record.vin
            if vin:
                record.model = vin[2:4]
            else:
                record.model = ""

    @api.depends('vin')
    def _compute_year(self):
        for record in self:
            vin = record.vin
            if vin:
                record.year = vin[4:6]
            else:
                record.year = ""

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