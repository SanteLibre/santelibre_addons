# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'SantéLibre data',
    'version': '0.1',
    'author': "MathBenTech",
    'website': 'https://mathben.tech',
    'license': 'AGPL-3',
    'category': 'Human Resources',
    'summary': 'SantéLibre data',
    'description': """
SantéLibre data
===============
All modules needed by SantéLibre.
""",
    'depends': [
        "helpdesk_service_call"
    ],
    'data': [
        "data/web_data.xml",
    ],
    "post_init_hook": "post_init_hook",
    'installable': True,
}
