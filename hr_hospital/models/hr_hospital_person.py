from odoo import models, fields

class HrHospitalPerson(models.AbstractModel):
    _name = 'hr.hospital.person'
    _description = 'Person'

    name = fields.Char(
        string='Name, Surname',
    )

    telephone = fields.Char(
        string='Phone number',
    )

    photo = fields.Binary(
        string='Photo',
    )

    sex = fields.Selection(
        values=[
            ('male', 'Male'),
                ('female', 'Female'),
        ],
    )
