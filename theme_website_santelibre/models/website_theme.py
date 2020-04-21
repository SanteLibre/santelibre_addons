from odoo import models


class WebsiteTheme(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_website_santelibre_post_copy(self, mod):
        # From Theme._post_copy
        self.disable_view('website_theme_install.customize_modal')
