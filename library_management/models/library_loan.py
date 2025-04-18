# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class LibraryLoan(models.Model):
    _name = "library.loan"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Library Loan"

    member_id = fields.Many2one("library.member", string="Member", required=True)
    book_id = fields.Many2one("library.book", string="Book", required=True)
    loan_date = fields.Date(string="Loan Date", default=fields.Date.context_today)
    return_date = fields.Date(string="Return Date")

    @api.constrains("book_id")
    def _check_book_availability(self):
        for loan in self:
            if loan.book_id.state != "available":
                raise ValidationError("Book is not available yet.")

    @api.model
    def create(self, vals):
        record_loan = super(LibraryLoan, self).create(vals)
        record_loan.book_id.state = "loaned"
        return record_loan

    def action_return_book(self):
        for loan in self:
            loan.book_id.state = "available"
            loan.return_date = fields.Date.context_today(self)
