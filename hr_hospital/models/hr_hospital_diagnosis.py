import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class HrHospitalDiagnosis(models.Model):
    """Model representing a medical diagnosis in the hospital system.
    
    This model stores information about diagnoses made during patient visits,
    including the associated disease, doctor, patient, and treatment plan.
    It also handles approval workflows for diagnoses made by intern doctors.
    """
    _name = 'hr.hospital.diagnosis'
    _description = 'Diagnosis'

    name = fields.Char()

    active = fields.Boolean(
        default=True,
        groups='base.group_system',
        copy=False,
    )

    visit_id = fields.Many2one(
        comodel_name='hr.hospital.visit',
        string='Patient visit',
        help='Visit',
    )

    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient',
        string='Patient',
        help='Patient',
    )

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Doctor',
        required=True,
        help='Doctor',
    )

    is_intern = fields.Boolean(
        related='doctor_id.is_intern',
        store=True,
    )

    disease_id = fields.Many2one(
        comodel_name='hr.hospital.disease',
        string='Disease',
    )

    disease_type = fields.Many2one(
        related='disease_id.type_id',
        store=True,
    )

    appointment_treatment = fields.Text(
        string='Appointment treatment',
        help='Write appointment treatment',
    )

    is_approved = fields.Boolean(
        string='Approved by mentor doctor',
    )

    @api.model
    def create(self, vals_list):
        """Create new diagnosis records with automatic approval for non-intern doctors.
        
        This method extends the standard create method to automatically approve
        diagnoses created by doctors who are not interns. Diagnoses created by
        intern doctors will need explicit approval from their mentors.
        
        Args:
            vals_list: Values for creating the new diagnosis records
            
        Returns:
            The newly created diagnosis records
        """
        records = super(HrHospitalDiagnosis, self).create(vals_list)
        for record in records:
            if not record.is_intern:
                record.is_approved = True
        return records
