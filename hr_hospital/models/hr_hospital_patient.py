import logging
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

logger = logging.getLogger(__name__)


class HrHospitalPatient(models.Model):

    _name = 'hr.hospital.patient'
    _inherit = 'hr.hospital.person.mixin'
    _description = 'Patient'

    active = fields.Boolean(
        default=True,
        groups='base.group_system',
        copy=False,
    )

    description = fields.Text(
        index=True,
        translate=True,
    )

    res_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Contact person',
    )

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Personal doctor'
    )

    disease_id = fields.Many2one(
        comodel_name='hr.hospital.disease',
        string="Disease",
        help="Disease",
    )

    passport_data = fields.Char(
        string='Passport data',
        help="Patient's passport data",
    )

    birthday_date = fields.Date(
        string='Date of birth',
        #  required=True,
        help="Patient's birthday",
    )

    age_count = fields.Integer(
        string='Age',
        compute='_compute_age',
        store=True,
        readonly=True,
        help="Patient's age",
    )

    diagnosis_count = fields.Integer(
        compute='_compute_diagnosis_count',
    )

    visit_count = fields.Integer(
        compute='_compute_visit_count',
    )

    @api.depends('birthday_date')
    def _compute_age(self):
        date_today = fields.Date.today()
        for patient in self:
            patient.age_count = str(relativedelta(date_today,
                                                  patient.birthday_date).years)

    def show_patient_visits(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Patient visits',
            'res_model': 'hr.hospital.visit',
            'view_mode': 'list',
            'view_type': 'form',
            'domain': [
                ["patient_id", "=", self.id],
            ],
        }

    def show_history_diagnosis(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'History of diagnosis',
            'res_model': 'hr.hospital.diagnosis',
            'target': 'current',
            'view_mode': 'list',
            'view_type': 'form',
            'domain': [
                ["patient_id", "=", self.id],
            ],
            'context': {'group_by': 'disease_id'},
        }

    def add_visit(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Add visit',
            'res_model': 'hr.hospital.visit',
            'target': 'new',
            'view_mode': 'form',
            'view_type': 'form',
            'context': {
                'default_patient_id': self.id,
                'quick_create': True,
            },
        }

    def _compute_diagnosis_count(self):
        for patient in self:
            model_name = 'hr.hospital.diagnosis'
            patient.diagnosis_count = self.env[model_name].search_count(
                domain=[
                    ('patient_id', '=', patient.id),
                ],
            )

    def _compute_visit_count(self):
        for patient in self:
            model_name = 'hr.hospital.visit'
            patient.visit_count = self.env[model_name].search_count(
                domain=[
                    ('patient_id', '=', patient.id),
                ],
            )
