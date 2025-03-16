from odoo import models, fields


# Визначення моделі для представлення типів захворювань у контексті лікарні
class HrHospitalDiseaseType(models.Model):
    # Назва моделі, яка використовується для ідентифікації в системі Odoo
    _name = 'hr.hospital.disease.type'

    # Опис моделі для довідкових цілей
    _description = "Disease type"

    # Поле для збереження назви типу захворювання
    # наприклад, "Інфекційне", "Хронічне"
    name = fields.Char()
