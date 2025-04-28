from odoo import models, fields


class HrHospitalPersonMixin(models.AbstractModel):
    """Abstract model that represents a person in the hospital system.
    
    This mixin provides common fields used across different types of people
    in the hospital system, such as patients and doctors.
    """
    _name = 'hr.hospital.person.mixin'
    _description = 'Person'
    _abstract = True

    name = fields.Char(
        string='Name, Surname',
    )

    telephone = fields.Char(
        string='Phone number',
    )

    photo = fields.Image(
        string='Photo of person',
    )

    gender = fields.Selection(
        selection=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other')
        ],
        default='other',
    )
