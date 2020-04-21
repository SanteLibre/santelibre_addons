# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo import _, api, SUPERUSER_ID

_logger = logging.getLogger(__name__)


def pre_init_hook(cr):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})

        # TODO delete all supported page
        # Remove all website pages before installing data
        website_page_ids = env['website.page'].search([])
        website_menu_ids = env['website.menu'].search([])
        # TODO website doesn't support multi
        # website_page_ids.website_id = None
        # TODO replace by :
        for website_page in website_page_ids:
            website_page.website_id = None
        for website_menu in website_menu_ids:
            website_menu.website_id = None
            website_menu.page_id = None
