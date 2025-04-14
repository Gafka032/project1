import logging

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

_logger = logging.getLogger(__name__)


class HrHospitalReportDiseases(models.TransientModel):
    _name = 'hr.hospital.report.diseases.wizard'
    _description = 'Diseases report'

    from_date = fields.Date(
        string='Date from',
        required=True,
        default=fields.Date.today().replace(day=1),
    )

    till_date = fields.Date(
        string='Date till',
        required=True,
        default=str(
            fields.Datetime.today() + relativedelta(months=+1, day=1, days=-1)
        )[:10],
    )

    doctor_ids = fields.Many2many(
        comodel_name='hr.hospital.doctor',
        string='Doctors',
    )

    disease_ids = fields.Many2many(
        comodel_name='hr.hospital.disease',
        string='Diseases',
    )

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        active_model = self.env.context.get('active_model')
        active_ids = self.env.context.get('active_ids')
        res['doctor_ids'] = self.env[active_model].browse(active_ids)
        return res

    def generate_report(self):
        domain=[
            ("create_date", ">", self.from_date),
            ("create_date", "<", self.till_date),
        ]

        if self.doctor_ids:
            domain.append(("doctor_id", "in", self.doctor_ids.ids))

        if self.disease_ids:
            domain.append(("disease_id", "in", self.disease_ids.ids))

        return {
            'type': 'ir.actions.act_window',
            'name': 'List diseases',
            'res_model': 'hr.hospital.diagnosis',
            'target': 'inline',
            'view_mode': 'list',
            'view_type': 'form',
            'domain': domain,
            'context': {'group_by': 'disease_id'},
        }
