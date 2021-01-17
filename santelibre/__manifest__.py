# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'SantéLibre',
    'version': '0.1',
    'author': "MathBenTech",
    'website': 'https://mathben.tech',
    'license': 'AGPL-3',
    'category': 'Human Resources',
    'summary': 'SantéLibre',
    'description': """
SantéLibre
==========
All modules needed by SantéLibre.
""",
    'depends': [
        # MathBenTech
        'website_sale',
    ],
    'data': [
        'data/res_partner_data.xml',
    ],
    'installable': True,
}
