# -*- coding: utf-8 -*-
from odoo import fields, models


class LibraryMember(models.Model):
    _name = "library.member"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Library Member"

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    membership_date = fields.Date(
        string="Membership Date", default=fields.Date.context_today
    )
