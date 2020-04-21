# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)


def post_init_hook(cr, e):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        values = {
            'auth_signup_reset_password': True,
            'group_use_lead': True,
            'website_name': "Le collectif SantéLibre",
            'favicon': env.ref("santelibre_data.favicon").datas,
            # 'theme_color_brand': "#002b2a",
            # 'theme_color_primary': "#2CD5C4",
            # 'branding_color_text': "#4c4c4c",
        }
        event_config = env['res.config.settings'].sudo().create(values)
        event_config.execute()
