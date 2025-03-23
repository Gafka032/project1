from odoo import models, fields

class HrHospitalPersonMixin(models.AbstractModel):
    _name = 'hr.hospital.person.mixin'
    _description = 'Person'

    name = fields.Char(
        string='Name, Surname',
    )

    telephone = fields.Char(
        string='Phone number',
    )

    photo = fields.Image(
        string='Photo',
    )

    gender = fields.Selection(
        values=[
            ('male', 'Male'),
            ('female', 'Female'),
        ],
    )

