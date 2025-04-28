import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HrHospitalDoctorSpeciality(models.Model):
    """Model representing medical specialities for doctors.
    
    This model stores information about different medical specialities
    that doctors can have, such as cardiology, neurology, pediatrics, etc.
    Each doctor in the system can be assigned to a speciality.
    """
    _name = 'hr.hospital.doctor.speciality'
    _description = 'Doctor speciality'

    name = fields.Char(
        string='Name of speciality',
    )

    active = fields.Boolean(
        default=True,
        copy=False,
    )

    description = fields.Text(
        index=True,
        translate=True,
    )
