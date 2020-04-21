# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'SantéLibre website data',
    'version': '0.1',
    'author': "MathBenTech",
    'website': 'https://mathben.tech',
    'license': 'AGPL-3',
    'category': 'Data',
    'summary': 'SantéLibre web data',
    'description': """
SantéLibre website data
=======================
All website data and pages needed by SantéLibre.
""",
    'depends': [
        "website",
        "website_form_builder",
        "muk_web_branding",
        #"muk_website_branding",
        "muk_mail_branding",
        "muk_web_theme_mail",
        #"muk_web_theme_website",
        #"muk_web_theme_branding",
        #"muk_web_theme_mobile",
    ],
    'data': [
        'data/website_data.xml',
        'views/footer_template.xml',
    ],
    "pre_init_hook": "pre_init_hook",
    "auto_install": False,
    "installable": True,
    "application": False,
}
