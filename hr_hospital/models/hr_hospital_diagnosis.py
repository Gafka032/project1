import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class HrHospitalDiagnosis(models.Model):
    _name = 'hr.hospital.diagnosis'
    _description = 'Diagnosis'

    name = fields.Char()

    active = fields.Boolean(
        default=True,
        groups='base.group_system',
        copy=False,
    )

    visit_id = fields.Many2one(
        comodel_name='hr.hospital.visit',
        string='Patient visit',
        help='Visit',
    )

    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient',
        string='Patient',
        help='Patient',
    )

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Doctor',
        required=True,
        help='Doctor',
    )

    is_intern = fields.Boolean(
        related='doctor_id.is_intern',
        store=True,
    )

    disease_id = fields.Many2one(
        comodel_name='hr.hospital.disease',
        string='Disease',
    )

    disease_type = fields.Many2one(
        related='disease_id.type_id',
        store=True,
    )

    appointment_treatment = fields.Text(
        string='Appointment treatment',
        help='Write appointment treatment',
    )

    is_approved = fields.Boolean(
        string='Approved by mentor doctor',
    )

    @api.model
    def create(self, vals_list):
        records = super(HrHospitalDiagnosis, self).create(vals_list)
        for record in records:
            if not record.is_intern:
                record.is_approved = True
        return records
