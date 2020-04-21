# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Theme website SantéLibre',
    'version': '0.1',
    'author': "MathBenTech",
    'website': 'https://mathben.tech',
    'license': 'AGPL-3',
    'category': 'Theme/Corporate',
    'sequence': 900,
    'summary': 'Theme website SantéLibre',
    'description': """
Theme website SantéLibre
========================
Theme website SantéLibre file
""",
    'depends': [
        "website",
        "website_theme_install",
    ],
    'data': [
        'data/theme_santelibre_data.xml',
        'views/theme_santelibre_templates.xml',
    ],
    'images': [
        'static/description/bootswatch.png',
        'static/description/bootswatch_screenshot.jpg',
    ],
    "auto_install": False,
    "installable": True,
    "application": False,
}
