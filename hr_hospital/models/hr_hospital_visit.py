import logging

from odoo import models, fields

class HrHospitalVisit(models.Model):
    _name = 'hr.hospital.visit'
    _description = 'Visit'