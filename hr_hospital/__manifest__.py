{
    'name': 'Hospital',
    'version': '17.0.1.0.0',
    'author': "Odoo School",
    'website': 'odoo.school',
    'license': 'OPL-1',
    'category': 'Human Resources',
    'depends':[
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_hospital_menu.xml',
        'views/hr_hospital_doctor_views.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'auto_install': False,
    'maintainer': "Danylo Senyuk",
    'images': ['static/desscription/icon.png',],
}