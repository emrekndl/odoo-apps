# Odoo Custom Modules Repository

![Odoo Version](https://img.shields.io/badge/Odoo-17.0-%23FF0000?style=flat-square)

This repository contains custom Odoo modules for various business needs.

---

## Included Modules

### 1. **Library Management**

Manage books, members, and loans with ease.  
 **Features**:

- Member-User synchronization
- Book availability tracking
- Loan period management
- User-specific access rules  
  **Screenshots**: [Library Members](screenshots/library_members.png) | [Loans](screenshots/loans.png)

---

## Installation

1. **Clone Repository**:

   ```bash
   git clone https://github.com/emrekndl/odoo-apps.git
   ```

2. **Install Modules**:

   - Copy desired module folders (e.g., `library_management`) to your Odoo addons directory.
   - Restart Odoo service.

3. **Enable in Odoo**:
   - Go to `Apps` → Search module name → Install.

---

## Screenshots

| Library Management               |
| -------------------------------- |
| ![Library](screenshots/lib1.png) |

---

**Tech Stack**:

- Odoo 17.0 (Python 3.11, PostgreSQL)
- XML views, Python models
- JavaScript for custom widgets

---

License

Distributed under the MIT License. See `LICENSE` for details.

---
