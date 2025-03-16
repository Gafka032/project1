from odoo import models, fields

class HrHospitalDiseaseType(models.Model):
    _name = 'hr.hospital.disease.type'
    _description = 'Disease Type'

    name = fields.Char()