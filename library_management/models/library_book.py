# -*- coding: utf-8 -*-
from odoo import models, fields


class LibraryBook(models.Model):
    _name = "library.book"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Library Book"

    name = fields.Char(string="Title", required=True)
    author = fields.Char(string="Author")
    isbn = fields.Char(string="ISBN")
    date_published = fields.Date(string="Date Published")

    state = fields.Selection(
        string="State",
        selection=[("available", "Available"), ("loaned", "Loaned")],
        default="available",
    )
