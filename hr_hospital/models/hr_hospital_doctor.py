from odoo import models, fields



class HrHospitalDoctor(models.Model):

    _name = 'hr.hospital.doctor'

    _description = 'Doctor'


    name = fields.Char()
