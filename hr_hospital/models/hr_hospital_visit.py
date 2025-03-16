from odoo import models, fields


# Оголошення класу HrHospitalVisit,
# який представляє модель "Візити в лікарню"
class HrHospitalVisit(models.Model):
    # Унікальне внутрішнє ім'я моделі в Odoo
    _name = 'hr.hospital.visit'
    # Короткий опис моделі, що використовується в інтерфейсі та документації
    _description = 'Visit'

    # Поле типу Char, яке зберігає назву або опис візиту
    name = fields.Char()
