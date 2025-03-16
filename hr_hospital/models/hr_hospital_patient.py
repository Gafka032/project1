from odoo import models, fields


# Клас HrHospitalPatient визначає модель
# для пацієнтів у системі управління лікарнею.
class HrHospitalPatient(models.Model):
    # Унікальне ім'я системної моделі,
    # яке використовується для ідентифікації цієї моделі в Odoo.
    _name = 'hr.hospital.patient'

    # Опис моделі, який з'являється у різних елементах інтерфейсу Odoo.
    _description = 'Patient'

    # Поле для збереження імені пацієнта. Тип поля — Char (текстовий рядок).
    name = fields.Char()

    # Багато-до-одного (Many2one) відношення
    # для зв'язку пацієнта з лікарем.
    # comodel_name визначає пов'язану модель ('hr.hospital.doctor').
    # string визначає назву цього поля у формі інтерфейсу.
    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Doctor'
    )

    # Багато-до-одного (Many2one) відношення
    # для зв'язування пацієнта з типом захворювання.
    # comodel_name вказує на модель,
    # що описує типи захворювань ('hr.hospital.disease.type').
    # string визначає відображення поля в інтерфейсі.
    disease_type_id = fields.Many2one(
        comodel_name='hr.hospital.disease.type',
        string="Disease type"
    )
