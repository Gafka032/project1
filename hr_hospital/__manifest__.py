{
    'name': 'Hospital',
    'version': '17.0.3.6.4',
    'author': "Odoo School",
    'website': 'https://odoo.school/',
    'license': 'OPL-1',
    'category': 'Human Resources',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',

        'wizard/hr_hospital_personal_doctor_wizard_views.xml',
        'wizard/hr_hospital_report_diseases_wizard_views.xml',

        'views/hr_hospital_visit_views.xml',
        'views/hr_hospital_diagnosis_views.xml',
        'views/hr_hospital_menu.xml',
        'views/hr_hospital_doctor_views.xml',
        'views/hr_hospital_doctor_speciality_views.xml',
        'views/hr_hospital_patient_views.xml',
        'views/hr_hospital_disease_views.xml',
        'views/hr_hospital_disease_type_views.xml',

        'data/hr.hospital.doctor.speciality.csv',
        'data/hr_hospital_disease_data.xml',
    ],
    'demo': [
        'demo/res_partner_demo.xml',
        'demo/hr.hospital.doctor.csv',
        'demo/hr.hospital.patient.csv',
        'demo/hr.hospital.visit.csv',
        'demo/hr.hospital.diagnosis.csv',
    ],
    'installable': True,
    'auto_install': False,
    'maintainer': "Danylo Senyuk",
    'images': ['static/desscription/icon.png',],
}
