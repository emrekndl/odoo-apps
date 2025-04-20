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
    days_taken = fields.Integer(
        string="Days Taken", compute="_compute_days_taken", store=True
    )

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
            # loan.return_date = fields.Date.context_today(loan)
            loan._compute_days_taken()
            template = self.env.ref("library_management.mail_template_return_thanks")
            if template:
                template.sudo().send_mail(loan.id, force_send=True)

    @api.depends("loan_date", "return_date")
    def _compute_days_taken(self):
        for rec in self:
            if rec.return_date and rec.loan_date:
                rec.days_taken = (rec.return_date - rec.loan_date).days
            else:
                rec.days_taken = 0

    def send_overdue_reminders(self):
        overdue_loans = self.search(
            [
                ("return_date", "<", fields.Date.context_today(self)),
                ("book_id.state", "=", "loaned"),
            ]
        )
        template = self.env.ref("library_management.mail_template_overdue_reminder")
        for loan in overdue_loans:
            if template:
                template.sudo().send_mail(loan.id, force_send=True)
