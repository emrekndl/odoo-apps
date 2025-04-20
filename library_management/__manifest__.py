# -*- coding: utf-8 -*-
{
    "name": "Library Management",
    "summary": "Library Management, simple application for odoo tutorial.",
    "description": """
        This module is a simple book management for book, member, loan.
    """,
    "author": "emrekndl",
    "website": "https://github.com/emrekndl",
    "category": "Tools",
    "version": "0.1",
    "license": "LGPL-3",
    "sequence": 1,
    "depends": ["base", "mail"],
    "data": [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "security/library_record_rules.xml",
        "data/add_user_to_group.xml",
        "data/return_thanks_mail_template_data.xml",
        "data/overdue_mail_template_data.xml",
        "data/overdue_ir_cron_data.xml",
        "views/library_book_views.xml",
        "views/library_member_views.xml",
        "views/library_loan_views.xml",
        "views/library_menu.xml",
        "reports/library_member_templates.xml",
        "reports/library_member_reports.xml",
    ],
    "demo": [
        "demo/demo.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}
