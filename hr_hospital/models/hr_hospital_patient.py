from odoo import models, fields

class HrHospitalPatient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Patient'

    name = fields.Char(string='Name')

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Doctor'
    )

    disease_type_id = fields.Many2one(
        comodel_name='hr.hospital.disease.type',
        string="Disease type"
    )