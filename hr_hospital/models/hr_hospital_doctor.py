from odoo import models, fields


# Модель для опису лікаря в системі Odoo
class HrHospitalDoctor(models.Model):
    # Унікальне ім'я моделі,
    # яке використовується для посилання на неї в базі даних
    _name = 'hr.hospital.doctor'
    # Короткий опис моделі
    _description = 'Doctor'

    # Поле для збереження імені лікаря
    name = fields.Char()
