# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

# import json


class LibraryController(http.Controller):
    @http.route(
        "/library/books", type="json", auth="public", methods=["GET"], csrf=False
    )
    def list_books(self, **kwargs):
        books = request.env["library.book"].sudo().search([])
        books_data = []
        for book in books:
            books_data.append(
                {
                    "id": book.id,
                    "name": book.name,
                    "author": book.author,
                    "isbn": book.isbn,
                    "date_published": book.date_published.strftime("%Y-%m-%d")
                    if book.date_published
                    else False,
                    "state": book.state,
                }
            )
        return {"status": "success", "data": books_data}

    @http.route(
        "/library/members", type="json", auth="public", methods=["GET"], csrf=False
    )
    def list_members(self, **kwargs):
        members = request.env["library.member"].sudo().search([])
        members_data = []
        for member in members:
            members_data.append(
                {
                    "id": member.id,
                    "name": member.name,
                    "email": member.email,
                    "phone": member.phone,
                    "membership_date": member.membership_date.strftime("%Y-%m-%d")
                    if member.membership_date
                    else False,
                }
            )
        return {"status": "success", "data": members_data}


"""
$ http get http://localhost:8069/library/members \
  jsonrpc="2.0" \
  method="call" \
  params:='{}' \
  id:=1

HTTP/1.1 200 OK
Connection: close
Content-Length: 388
Content-Type: application/json; charset=utf-8
Date: Wed, 16 Apr 2025 21:51:58 GMT
Server: Werkzeug/2.2.2 Python/3.11.11
Set-Cookie: session_id=04bc2a9cad22d43a5330d409ed26edcb17a99b88; Expires=Thu, 16 Apr 2026 21:51:58 GMT; Max-Age=604800; HttpOnly; Path=/
X-Content-Type-Options: nosniff

{
    "id": 1,
    "jsonrpc": "2.0",
    "result": {
        "data": [
            {
                "email": "jd@mail.com",
                "id": 1,
                "membership_date": "2025-04-16",
                "name": "John Doe",
                "phone": false
            },
            {
                "email": "rm@mail.com",
                "id": 2,
                "membership_date": "2025-04-15",
                "name": "Robert Musk",
                "phone": false
            },
            {
                "email": "ph@mail.com",
                "id": 3,
                "membership_date": "2025-04-14",
                "name": "Paul Holmes",
                "phone": false
            }
        ],
        "status": "success"
    }
}

"""
