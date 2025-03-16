import logging

from odoo import models, fields

class HrHospitalPatient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Patient'