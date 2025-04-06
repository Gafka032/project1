import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HrHospitalDoctor(models.Model):

    _name = 'hr.hospital.doctor'
    _inherit = 'hr.hospital.person.mixin'
    _description = 'Doctor'


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
        domain="[('is_intern', '=', False)]",
        help="Intern's mentor",
    )

    mentor_phone = fields.Char(
        related='mentor_id.telephone',
        string='Mentor phone',
    )

    mentor_photo = fields.Image(
        related='mentor_id.photo',
        string='Mentor photo',
    )

    intern_ids = fields.One2many(
        comodel_name='hr.hospital.doctor',
        inverse_name='mentor_id',
        string='Interns',
        readonly=True,
    )
