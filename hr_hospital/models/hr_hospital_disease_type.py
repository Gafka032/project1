import logging

from odoo import models, fields, api, exceptions

_logger = logging.getLogger(__name__)


class HrHospitalDiseaseType(models.Model):
    _name = 'hr.hospital.disease.type'
    _description = 'Disease type'
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char(
        string='Name of disease type',
        index='trigram',
        required=True,
    )

    complete_name = fields.Char(
        string='Complete Name of disease type',
        compute='_compute_complete_name',
        recursive=True,
        store=True,
    )

    parent_id = fields.Many2one(
        comodel_name='hr.hospital.disease.type',
        string='Parent type',
        index=True,
        ondelete='cascade'
    )

    parent_path = fields.Char(
        index=True,
        unaccent=False
    )

    child_id = fields.One2many(
        comodel_name='hr.hospital.disease.type',
        inverse_name='parent_id',
        string='Child types'
    )

    @api.constrains('parent_id')
    def _check_category_recursion(self):
        if not self._check_recursion():
            raise exceptions.ValidationError_('You cannot create recursive '
                                              'categories.')

    @api.model
    def name_create(self, name):
        category = self.create({'name': name})
        return category.id, category.display_name

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = '%s / %s' % (
                    category.parent_id.complete_name, category.name
                )
            else:
                category.complete_name = category.name
