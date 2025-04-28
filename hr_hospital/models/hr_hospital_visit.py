import logging

from odoo import models, fields, api, exceptions, _

_logger = logging.getLogger(__name__)


class HrHospitalVisit(models.Model):
    """Model representing a hospital visit.
    
    This model stores information about patient visits to the hospital,
    including scheduled and actual visit dates, the assigned doctor,
    and related diagnoses.
    """
    _name = 'hr.hospital.visit'

    _description = 'Visit'

    active = fields.Boolean(
        default=True,
        groups='base.group_system',
        copy=False,
    )

    description = fields.Text(
        index=True,
        translate=True,
        help="Visit description",
    )

    state = fields.Selection(
        selection=[
            ('scheduled', 'Scheduled'),
            ('completed', 'Completed'),
            ('canceled', 'Cancelled'),
        ],
        default='scheduled',
        help="Visit state",
    )

    scheduled_visit_date = fields.Datetime(
        string='The planned visit date and time',
        help="The planned visit date and time",
    )

    visit_date = fields.Datetime(
        string='The actual visit date and time',
    )

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Doctor',
    )

    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient',
        string='Patient',
    )

    diagnosis_id = fields.One2many(
        comodel_name='hr.hospital.diagnosis',
        inverse_name='visit_id',
        string='Diagnosis',
    )

    @api.ondelete(at_uninstall=False)
    def _ondelete(self):
        """Prevent deletion of visits that have associated diagnoses.
        
        Raises:
            UserError: If the visit has associated diagnoses.
        """
        self.ensure_one()
        if self.diagnosis_id:
            raise exceptions.UserError(_("You cannot delete visit with "
                                        "diagnosis."))

    @api.constrains('scheduled_visit_date', 'doctor_id', 'patient_id')
    def _constrains_scheduled_visit_date_doctor_patient(self):
        """Ensure a patient cannot have multiple visits on the same day.
        
        This constraint checks if there are any other visits for the same patient
        with the same doctor on the same day as the scheduled visit date.
        
        Raises:
            UserError: If another visit for the same patient exists on the same day.
        """
        self.ensure_one()
        start_date = self.scheduled_visit_date.strftime("%Y-%m-%d 00:00:00")
        end_date = self.scheduled_visit_date.strftime("%Y-%m-%d 23:59:59")
        result_count = self.env['hr.hospital.visit'].search_count(
            domain=[
                ('doctor_id', '=', self.doctor_id.id),
                ('patient_id', '=', self.patient_id.id),
                ('scheduled_visit_date', '>', start_date),
                ('scheduled_visit_date', '<', end_date),
                ('id', '!=', self.id),
            ]
        )
        if result_count != 0:
            raise exceptions.UserError(
                _("One patient cannot have two visits "
                  "at the same day."))

    @api.constrains('visit_date', 'doctor_id', 'state')
    def _constrains_visit_date_doctor_id_state(self):
        """Prevent changing visit date for completed visits in the past.
        
        This constraint ensures that the visit date cannot be changed
        for visits that are marked as completed and scheduled in the past.
        
        Raises:
            ValidationError: If attempting to change the date of a completed visit
                            that was scheduled in the past.
        """
        self.ensure_one()
        today_date = fields.Datetime.today().strftime("%Y-%m-%d")
        start_date = self.scheduled_visit_date.strftime("%Y-%m-%d 00:00:00")
        if self.state == 'completed' and start_date < today_date:
            raise exceptions.ValidationError(
                _("It is not possible to change "
                  "the visit date after the visit "
                  " is completed."))

    @api.constrains('active')
    def _constrains_active(self):
        """Prevent archiving visits that have associated diagnoses.
        
        This constraint ensures that visits with diagnoses cannot be archived,
        maintaining data integrity and preventing orphaned diagnosis records.
        
        Raises:
            UserError: If attempting to archive a visit with associated diagnoses.
        """
        self.ensure_one()
        if not self.active and self.diagnosis_id:
            raise exceptions.UserError(
                _("You cannot archive visit with "
                  "diagnosis."))
