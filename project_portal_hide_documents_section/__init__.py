from odoo import api, SUPERUSER_ID
import logging

_logger = logging.getLogger(__name__)


def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    view = env["ir.ui.view"].search(
        [("key", "=", "project.portal_my_home"), ("active", "=", False)]
    )
    if view:
        view.active = True
        _logger.info(
            "Re-activated 'project.portal_my_home' view during module uninstall."
        )
