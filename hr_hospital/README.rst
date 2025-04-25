Hospital Management System
=======================

.. image:: https://img.shields.io/badge/license-OPL--1-blue.svg
   :target: https://www.odoo.com/documentation/user/17.0/legal/licenses/licenses.html
   :alt: License: OPL-1

.. image:: https://img.shields.io/badge/version-17.0.3.9.5-green.svg
   :alt: Version: 17.0.3.9.5

.. image:: https://img.shields.io/badge/Odoo-17.0-brightgreen.svg
   :target: https://github.com/odoo/odoo/tree/17.0
   :alt: Odoo Support

.. image:: https://img.shields.io/badge/python-3.10+-blue.svg
   :target: https://www.python.org/downloads/release/python-3107/
   :alt: Python Version

.. image:: https://img.shields.io/badge/integration-calendar%20%7C%20SMS%20%7C%20email-lightgrey
   :alt: Integrations

|

The Hospital Management System module offers a comprehensive solution for managing medical processes in healthcare facilities of any scale: from small private clinics to large multi-profile medical centers.

----

Latest Updates (v17.0.3.9.5)
============================

.. image:: static/description/img/update_banner.png
   :alt: New Features in Version 17.0.3.9.5
   :width: 100%

* ⚡ **Interactive Analytics**: Advanced reporting system with dynamic filters and data visualization
* 🩺 **Advanced Patient Management**: Enhanced medical records with complete treatment history
* 📊 **Effectiveness Analysis**: Intelligent system for evaluating treatment method outcomes
* 📅 **Smart Scheduling**: Improved doctor schedule management with calendar integration
* 🌍 **Full Localization**: Multilingual interface with professional translations
* 🔒 **Reliable Protection**: Multi-level security system with medical data encryption
* 📘 **Comprehensive Documentation**: Complete API documentation with integration examples for developers

Key Features
===========

.. image:: static/description/img/features_banner.png
   :alt: Key Module Features
   :width: 100%

**Comprehensive Patient Management**
-----------------------------------
* Unified electronic medical record for each patient
* Detailed history of visits and treatments with chronological timeline
* Personal doctor assignment and visit tracking
* Diagnosis and treatment plan management
* Convenient patient data search and filtering

**Effective Doctor Management**
------------------------------
* Tracking specializations and qualifications of medical staff
* Smart schedule planning with conflict avoidance
* Analysis of workload and performance effectiveness
* Optimization of patient distribution among specialists
* Calendar integration for appointment synchronization

**Advanced Diagnostic System**
----------------------------
* Comprehensive disease catalog with hierarchical structure
* Tracking symptom dynamics and treatment effectiveness
* Linking diagnoses with visits and prescribed procedures
* Support for international treatment protocols
* Epidemiological situation analysis and disease statistics

**Intelligent Analytics and Reporting**
-------------------------------------
* Interactive dashboards with key performance indicators
* Flexible filter system for analytical report generation
* Disease statistics across various parameters
* Treatment method effectiveness analysis and outcomes
* Data export in various formats for further analysis

**Reliable Security System**
--------------------------
* Multi-level role-based access control
* Detailed audit logs of all user actions in the system
* Encryption of confidential medical data
* Compliance with international medical information protection standards
* Flexible data visibility settings for different staff categories

Module Architecture
=================

.. code-block:: text

    hr_hospital/
    ├── models/                    # Core data models
    │   ├── hr_hospital_patient.py       # Patient model
    │   ├── hr_hospital_doctor.py        # Doctor model
    │   ├── hr_hospital_visit.py         # Visit model
    │   ├── hr_hospital_diagnosis.py     # Diagnosis model
    │   ├── hr_hospital_disease.py       # Disease model
    │   ├── hr_hospital_doctor_speciality.py  # Doctor specialties
    │   └── hr_hospital_person_mixin.py  # Base class for persons
    │
    ├── views/                     # Model views
    │   ├── hr_hospital_patient_views.xml      # Patient interface
    │   ├── hr_hospital_doctor_views.xml       # Doctor interface
    │   ├── hr_hospital_visit_views.xml        # Visit management
    │   ├── hr_hospital_diagnosis_views.xml    # Work with diagnoses
    │   ├── hr_hospital_disease_views.xml      # Disease catalog
    │   └── hr_hospital_menu.xml               # Main module menu
    │
    ├── wizards/                   # Wizards for complex operations
    │   ├── hr_hospital_personal_doctor_wizard.py    # Doctor change
    │   ├── hr_hospital_report_diseases_wizard.py    # Reporting
    │   └── hr_hospital_treatment_plan_wizard.py     # Treatment plans
    │
    ├── security/                  # Module security system
    │   ├── ir.model.access.csv               # Model access rights
    │   ├── hr_hospital_security_groups.xml   # Security groups
    │   └── hr_hospital_security_rules.xml    # Record access rules
    │
    ├── data/                      # Base module data
    │   ├── hr_hospital_disease_data.xml      # Typical diseases
    │   └── hr.hospital.doctor.speciality.csv # Doctor specialties
    │
    ├── reports/                   # Reporting system
    │   ├── hr_hospital_patient_report.xml     # Patient reports
    │   ├── hr_hospital_disease_report.xml     # Disease analysis
    │   └── hr_hospital_doctor_report.xml      # Doctor statistics
    │
    ├── static/                    # Static resources
    │   └── description/                      # Module description
    │       ├── index.html                    # Description main page
    │       └── icon.png                      # Module icon
    │
    ├── demo/                      # Demo data
    │   └── hr_hospital_demo.xml             # Sample records
    │
    ├── i18n/                      # Translations
    │   ├── hr_hospital.pot                  # Base translation file
    │   └── uk_UA.po                         # Ukrainian translation
    │
    ├── tests/                     # Automated tests
    │   ├── test_patient.py                  # Patient tests
    │   └── test_visit.py                    # Visit tests
    │
    ├── __init__.py                # Module initialization
    ├── __manifest__.py            # Module description and dependencies
    ├── README.rst                 # Developer documentation
    └── changelog.rst              # Module change history

Installation
===========

.. code-block:: bash

    # Clone repository
    git clone https://github.com/odoo-school/hr_hospital.git
    
    # Copy module to Odoo addons folder
    cp -r hr_hospital /path/to/odoo/addons/
    
    # Update module list in Odoo
    # and install module through interface

You can also install the module directly through the Odoo interface:

1. Go to **Apps** menu
2. Click **Update Apps List**
3. Find "Hospital Management System" in search
4. Click **Install**

.. note::
   The module depends only on the standard 'base' module and requires no additional dependencies

Configuration
============

After installation, it is recommended to complete the following steps:

1. **Security Setup**
   
   * Go to *Settings → Users & Companies → Groups*
   * Assign appropriate access rights to hospital data for different users

2. **Reference Data Population**
   
   * Add or edit doctor specialties in the *Hospital → References → Specialties* section
   * Configure the disease catalog in the *Hospital → References → Diseases* section

3. **Interface Personalization**
   
   * Customize form and report views according to your facility's needs
   * Define typical treatment plans for common diseases

Usage
=====

.. image:: static/description/img/interface_preview.png
   :alt: Module Interface
   :width: 100%

Patient Management
-----------------

For effective patient management:

1. Go to **Hospital → Patients**
2. Create a new patient by filling in the required fields
3. Assign a personal doctor and specify a contact person
4. Use the **Add Visit** button to create a new appointment
5. View diagnosis history through the **Diagnoses** tab

Visit Scheduling
---------------

The system offers a convenient interface for scheduling visits:

1. In the patient form, click the **Add Visit** button
2. Select the date and time for the visit
3. The system will automatically check doctor availability
4. After completing the visit, add a diagnosis and prescriptions
5. Use the **Visit Calendar** for a general schedule overview

Working with Diagnoses
--------------------

For maintaining disease history:

1. Go to **Hospital → Diagnoses**
2. Create a new diagnosis by selecting a patient and disease
3. Specify diagnosis details and treatment plan
4. Track the effectiveness of the prescribed treatment
5. Analyze the patient's diagnosis history in the "Diagnosis History" section

Analytics and Reporting
---------------------

To obtain analytical data:

1. Go to **Hospital → Reports**
2. Select the report type (patients, diseases, doctor effectiveness)
3. Configure filters to obtain targeted information
4. Export results in a convenient format (PDF, Excel, etc.)
5. Use dashboards for regular monitoring of indicators

Integration and Extension
=======================

The module is developed using modern Odoo architecture, providing:

* Easy integration with other Odoo modules
* Ability to extend functionality through inheritance mechanisms
* REST API support for integration with external systems
* Complete API documentation with examples for developers
* Capability to create custom reports and analytics

.. code-block:: python

    # Example of extending module functionality
    class ExtendedPatient(models.Model):
        _inherit = 'hr.hospital.patient'
        
        insurance_number = fields.Char(string="Insurance Policy Number")
        blood_type = fields.Selection([
            ('a+', 'A+'), ('a-', 'A-'),
            ('b+', 'B+'), ('b-', 'B-'),
            ('ab+', 'AB+'), ('ab-', 'AB-'),
            ('o+', 'O+'), ('o-', 'O-'),
        ], string="Blood Type")

Technical Support
================

If you have questions or issues:

* Review the documentation on `GitHub Wiki <https://github.com/odoo-school/hr_hospital/wiki>`_
* Create a request on `GitHub Issues <https://github.com/odoo-school/hr_hospital/issues>`_
* Contact the module authors: support@odoo.school

License
=======

This module is distributed under the OPL-1 license (Odoo Proprietary License v1.0).
Detailed information is available in the LICENSE file and on the official Odoo website.

About the Authors
===============

The module was developed by the Odoo School team from Ukraine.

**Contacts:**

* Website: https://odoo.school/
* Email: info@odoo.school
* GitHub: https://github.com/odoo-school

**Developers:**

* Danylo Senyuk - Technical Architect and Lead Developer
* Odoo School Team - Development and Testing

.. raw:: html

    <div style="text-align: center; margin-top: 40px;">
        <a href="https://odoo.school/" target="_blank">
            <img src="static/description/img/odoo_school_logo.png" alt="Odoo School" width="250px">
        </a>
    </div>