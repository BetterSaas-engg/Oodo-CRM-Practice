from odoo import models, fields, api

class EeliElevator(models.Model):
    _name = 'eel.elevator'
    _description = 'Elevator Asset Registry'

    # 1. General & Technical Info
    name = fields.Char(string='Device ID', required=True)
    serial_no = fields.Char(string='Serial No of Service Job')
    tssa_license = fields.Char(string='TSSA License Number')
    make = fields.Char(string='Make')
    model_ref = fields.Char(string='Model & Reference')
    no_devices = fields.Integer(string='No. of Devices', default=1)
    device_type = fields.Selection([
        ('lula', 'LULA'),
        ('passenger', 'Passenger'),
        ('freight', 'Freight'),
        ('dumbwaiter', 'Dumbwaiter'),
        ('vpl', 'VPL/IPL'),
        ('scissor', 'Scissor Lift')
    ], string='Device Type')
    
    # 2. Key Dates
    handover_date = fields.Date(string='Handover Date')
    contract_start = fields.Date(string='Contract Start Date')
    contract_end = fields.Date(string='Contract End Date')
    cat1_date = fields.Date(string='CAT1 Date')
    cat5_date = fields.Date(string='CAT5 Date')

    # 3. Contract & Status
    visits_count = fields.Integer(string='Number of Visits')
    service_route = fields.Char(string='Service Route')
    contract_status = fields.Selection([
        ('active', 'Active'),
        ('not_active', 'Not Active')
    ], string='Contract Status', default='active')
    payment_status = fields.Selection([
        ('free', 'Free'),
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid')
    ], string='Payment Status')

    # 4. Pricing Details (Monetary fields for Finance)
    annual_price = fields.Float(string='Annual Contract Price')
    price_per_visit = fields.Float(string='Price Per Visit')
    callback_single_edm = fields.Float(string='Callback Single Mechanic')
    callback_crew = fields.Float(string='Callback Crew')
    annual_phone_line = fields.Float(string='Annual Phone Line')
    annual_camera_monitoring = fields.Float(string='Annual Camera Monitoring')
    cat1_charge = fields.Float(string='CAT1 Charge')
    cat5_charge = fields.Float(string='CAT5 Charge')

    # 5. Relationship to Odoo Contacts
    owner_id = fields.Many2one('res.partner', string='Customer/Owner')
    site_address = fields.Char(string='Site Address')

class ResPartner(models.Model):
    _inherit = 'res.partner'

    eeli_project_no = fields.Char(string='Project No. EELI')
    service_job_no = fields.Char(string='Service Job No')
    job_name = fields.Char(string='Job Name')