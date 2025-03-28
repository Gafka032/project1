import logging
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

logger = logging.getLogger(__name__)


class HrHospitalPatient(models.Model):

    _name = 'hr.hospital.patient'
    _inherit = 'hr.hospital.person.mixin'
    _description = 'Patient'

    name = fields.Char(
        string="Patient's name",
        help="Patient's name and surname",
    )

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

    disease_type_id = fields.Many2one(
        comodel_name='hr.hospital.disease.type',
        string="Disease type",
        help="Disease type",
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

    @api.depends('birthday_date')
    def _compute_age(self):
        for record in self:
            if record.birthday_date:
                record.age_count = relativedelta(self.env.context['today'],
                                                 record.birthday_date).years
