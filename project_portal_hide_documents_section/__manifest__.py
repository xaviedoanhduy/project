# Copyright 2025 Kencove (https://www.kencove.com).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Project Portal Hide Documents Section",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "summary": """Hide Project and Tasks document section on customer portal.""",
    "depends": ["project"],
    "author": "Kencove, " "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/project",
    "category": "Project",
    "data": ["views/project_portal_templates.xml"],
    "installable": True,
    "uninstall_hook": "uninstall_hook",
}
