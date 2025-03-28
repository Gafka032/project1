import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HrHospitalPersonalDoctorWizard(models.TransientModel):
    _name = 'hr.hospital.personal.doctor.wizard'
    _description = 'Mass redefinition of the personal doctor for patients'

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Personal doctor',
    )

    def change_personal_doctor(self):
        active_model = self.env.context.get('active_model')
        active_ids = self.env.context.get('active_ids')
        for active_id in active_ids:
            patient = self.env[active_model].browse(active_id)
            patient.doctor_id = self.doctor_id
