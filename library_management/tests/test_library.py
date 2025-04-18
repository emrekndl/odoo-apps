from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestLibraryManagement(TransactionCase):
    def setUp(self):
        super(TestLibraryManagement, self).setUp()
        self.book_model = self.env["library.book"]
        self.member_model = self.env["library.member"]
        self.loan_model = self.env["library.loan"]

        self.book = self.book_model.create(
            {
                "name": "Odoo Docs",
                "author": "John Doe",
                "isbn": "1234567890",
                "state": "available",
            }
        )

        self.member = self.member_model.create(
            {
                "name": "Robert Urban",
                "email": "robert@example.com",
                "phone": "5551234567",
            }
        )

    def test_create_loan_updates_book_state(self):
        loan = self.loan_model.create(
            {
                "member_id": self.member.id,
                "book_id": self.book.id,
            }
        )
        self.assertEqual(
            self.book.state, "borrowed", "Book after loan creation should be 'borrowed'"
        )

        loan.action_return()
        self.assertEqual(
            self.book.state, "available", "Book after return should be 'available'"
        )
        self.assertTrue(loan.return_date, "Return date should be set")

    def test_loan_constrains_prevent_double_loan(self):
        self.loan_model.create(
            {
                "member_id": self.member.id,
                "book_id": self.book.id,
            }
        )
        with self.assertRaises(ValidationError):
            self.loan_model.create(
                {
                    "member_id": self.member.id,
                    "book_id": self.book.id,
                }
            )
