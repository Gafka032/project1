import logging

from odoo import models, fields, api, exceptions

_logger = logging.getLogger(__name__)


class HrHospitalDiseaseType(models.Model):
    """Model representing disease types in a hierarchical structure.
    
    This model implements a tree structure for disease types, allowing for
    parent-child relationships between different categories of diseases.
    It provides functionality for managing the hierarchy and computing
    complete names that include the full path in the hierarchy.
    """
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
        """Prevent recursive category hierarchies.
        
        This constraint ensures that a disease type cannot be its own ancestor,
        which would create an invalid recursive hierarchy.
        
        Raises:
            ValidationError: If a recursive hierarchy is detected.
        """
        if not self._check_recursion():
            raise exceptions.ValidationError_('You cannot create recursive '
                                              'categories.')

    @api.model
    def name_create(self, name):
        """Create a new disease type using only a name.
        
        This method simplifies the creation of disease types by allowing them
        to be created with just a name value, without specifying other fields.
        
        Args:
            name: The name for the new disease type
            
        Returns:
            tuple: (id, display_name) of the newly created disease type
        """
        category = self.create({'name': name})
        return category.id, category.display_name

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        """Compute the complete name of a disease type including its hierarchy.
        
        This method builds a complete name for each disease type by concatenating
        the names of all its ancestors, separated by slashes. For example,
        if 'Viral' is a child of 'Infectious', its complete name would be
        'Infectious / Viral'.
        """
        for category in self:
            if category.parent_id:
                category.complete_name = '%s / %s' % (
                    category.parent_id.complete_name, category.name
                )
            else:
                category.complete_name = category.name
