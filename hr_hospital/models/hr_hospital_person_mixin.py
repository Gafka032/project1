from odoo import models, fields

class HrHospitalPersonMixin(models.AbstractModel):
    _name = 'hr.hospital.person.mixin'
    _description = 'Person'
    _abstract = True

    person_name = fields.Char(
        string='Name, Surname',
    )

    telephone = fields.Char(
        string='Phone number',
    )

    photo = fields.Image(
        string='Photo',
    )

    gender = fields.Selection(
        selection=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other')
        ],
        default='other',
    )

