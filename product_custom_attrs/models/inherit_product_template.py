# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class InheritProductTemplate(models.Model):
    """Product Template Fields"""

    _inherit = "product.template"

    markup = fields.Float(string="Markup", digits=(4, 2))

    @api.constrains("markup")
    def _check_markup(self):
        for rec in self:
            if mp := rec.markup:
                if mp < 0:
                    raise ValidationError(
                        _("Invalid Markup Value: Markup cannot be negative.")
                    )
