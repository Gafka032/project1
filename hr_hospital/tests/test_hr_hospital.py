from odoo import fields
from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError, ValidationError
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta



class TestHrHospital(TransactionCase):
    """Test class for checking hr_hospital models."""

    def setUp(self):
        """Initializing the initial data for all tests."""
        super(TestHrHospital, self).setUp()
        
        # Creating test data
        self.doctor = self.env['hr.hospital.doctor'].create({
            'name': 'Doctor Test',
            'telephone': '+380991234567',
        })
        
        self.patient = self.env['hr.hospital.patient'].create({
            'name': 'Patient Test',
            'telephone': '+380997654321',
            'birthday_date': '1990-01-01',
            'doctor_id': self.doctor.id,
        })
        
        tomorrow = datetime.now() + timedelta(days=1)
        self.visit = self.env['hr.hospital.visit'].create({
            'doctor_id': self.doctor.id,
            'patient_id': self.patient.id,
            'scheduled_visit_date': tomorrow.strftime('%Y-%m-%d %H:%M:%S'),
            'description': 'Test visit',
            'state': 'scheduled',
        })

    def test_compute_age(self):
        """Test to verify patient age calculation."""
        today = fields.Date.today()

        # Testing different dates of birth
        for birthday in ['2000-01-01', '1990-05-15', '1985-12-31']:
            self.patient.write({'birthday_date': birthday})
            birth_date = fields.Date.to_date(birthday)
            expected_age = relativedelta(today, birth_date).years

        self.assertEqual(
            int(self.patient.age_count),
            expected_age,
            f"Incorrect age calculation for date of birth {birthday}"
        )

    def test_visit_constraints(self):
        """Test to check visit restrictions."""
        # Trying to create two visits in one day for one patient and doctor
        tomorrow = datetime.now() + timedelta(days=1)
        tomorrow_str = tomorrow.strftime('%Y-%m-%d %H:%M:%S')
        
        # The first visit has already been created in setUp()
        
        # Attempting to create a second visit on the same day
        with self.assertRaises(UserError):
            self.env['hr.hospital.visit'].create({
                'doctor_id': self.doctor.id,
                'patient_id': self.patient.id,
                'scheduled_visit_date': tomorrow_str,
                'description': 'Second test visit',
                'state': 'scheduled',
            })

    def test_visit_deletion_with_diagnosis(self):
        """Test to check whether a visit with a diagnosis is prohibited from being deleted."""
        # Creating a test diagnosis
        diagnosis = self.env['hr.hospital.diagnosis'].create({
            'visit_id': self.visit.id,
            'patient_id': self.patient.id,
            'doctor_id': self.doctor.id,
        })
        
        # Attempt to delete a visit with a diagnosis
        with self.assertRaises(UserError):
            self.visit.unlink()