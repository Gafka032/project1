from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class HrHospitalDoctor(models.Model):

    _name = 'hr.hospital.doctor'
    _inherit = 'hr.hospital.person.mixin'
    _description = 'Doctor'

    name = fields.Char(
        string='Name, Surname',
        help="Doctor's name",
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
        string='Contact'
    )

    speciality_id = fields.Many2one(
        comodel_name='hr.hospital.doctor.speciality',
        string='Speciality',
        help="Doctor's speciality"
    )

    is_intern = fields.Boolean(
        help="Is doctor an intern?",
        default=False,
        copy=False,
    )

    mentor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Mentor',
        domain="[('is_intern', '=', True)]",
        help="Intern's mentor",
    )