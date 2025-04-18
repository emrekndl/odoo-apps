# -*- coding: utf-8 -*-
from odoo import api, fields, models


class LibraryMember(models.Model):
    _name = "library.member"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Library Member"
    _rec_name = "user_id"

    user_id = fields.Many2one(
        "res.users",
        string="Odoo User",
        ondelete="cascade",
        help="The Odoo user linked to the member.",
    )
    email = fields.Char(string="Email", related="user_id.email", readonly=True)
    phone = fields.Char(string="Phone", releated="user.phone", readonly=True)
    membership_date = fields.Date(
        string="Membership Date", default=fields.Date.context_today
    )

    @api.model
    def create(self, vals_list):
        member = super().create(vals_list)
        if member.user_id:
            member.user_id.sudo().write(
                {
                    "groups_id": [
                        (4, self.env.ref("library_management.group_library_user").id)
                    ]
                }
            )

        return member
