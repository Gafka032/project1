{
    'name': 'Hospital',
    'version': '17.0.2.3.7',
    'author': "Odoo School",
    'website': 'https://odoo.school/',
    'license': 'OPL-1',
    'category': 'Human Resources',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_hospital_menu.xml',
        'views/hr_hospital_doctor_views.xml',
        'views/hr_hospital_patient_views.xml',
        'views/hr_hospital_disease_views.xml',
        'views/hr_hospital_disease_type_views.xml',
        'data/hr_hospital_disease_type_data.xml',
    ],
    'demo': [
        'demo/hr_hospital_doctor_demo.xml',
        'demo/hr.hospital.patient.csv',
    ],
    'installable': True,
    'auto_install': False,
    'maintainer': "Danylo Senyuk",
    'images': ['static/desscription/icon.png',],
}
