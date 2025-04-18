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
        "views/library_book_views.xml",
        "views/library_member_views.xml",
        "views/library_loan_views.xml",
        "reports/library_reports.xml",
        "views/library_menu.xml",
        "views/templates.xml",
    ],
    "demo": [
        "demo/demo.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}
