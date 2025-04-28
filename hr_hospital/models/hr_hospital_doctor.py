import logging
import string

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HrHospitalDoctor(models.Model):
    """Model representing a hospital doctor.
    
    This model stores information about doctors in the hospital system,
    including their personal details, specialities, and relationships
    with interns and mentors.
    """

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

    def _get_report_base_filename(self):
        """Generate a base filename for reports related to this doctor.
        
        Returns:
            str: A filename string containing the doctor's name and speciality.
        """
        file_name = string.Template('$name($speciality)')
        return file_name.substitute(
            name=self.name,
            speciality=self.speciality_id.name,
        )

    def add_visit(self):
        """Open a form to quickly add a new visit.
        
        Returns:
            dict: Action dictionary to open a new visit form in quick create mode.
        """
        return {
            'type': 'ir.actions.act_window',
            'name': 'Quick add visit',
            'res_model': 'hr.hospital.visit',
            'target': 'new',
            'view_mode': 'form',
            'view_type': 'form',
            'context': {
                'quick_create': True,
            },
        }
