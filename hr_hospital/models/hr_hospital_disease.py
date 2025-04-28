import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HrHospitalDisease(models.Model):
    """Model representing diseases in the hospital system.
    
    This model stores information about different diseases that can be diagnosed,
    including their names, descriptions, and categorization by disease type.
    """
    _name = 'hr.hospital.disease'
    _description = 'Types of diseases (diseases)'

    name = fields.Char()

    active = fields.Boolean(
        default=True,
        groups='base.group_system',
        copy=False,
    )

    description = fields.Text(
        index=True,
        translate=True,
    )

    type_id = fields.Many2one(
        comodel_name='hr.hospital.disease.type',
        string='Disease type',
        required=True
    )
