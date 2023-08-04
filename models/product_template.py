from odoo import models, api
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def create(self, values):
        user = self.env.user
        if user.has_group('mo_restrict_create_edit.restrict_product_template'):
            raise UserError("You do not have permission to create products.")
        return super(ProductTemplate, self).create(values)

    def write(self, values):
        user = self.env.user
        if user.has_group('mo_restrict_create_edit.restrict_product_template'):
            raise UserError("You do not have permission to update products.")
        return super(ProductTemplate, self).write(values)
