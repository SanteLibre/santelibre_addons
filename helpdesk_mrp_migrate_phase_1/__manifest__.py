{
    'name': 'Helpdesk MRP migration phase 1',
    'category': 'Website',
    'summary': 'Migrate phase 1 SantéLibre of mrp integration',
    'version': '12.0.0.0',
    'description': """
Transform human text in corresponding machine. Change color of xml show of ticket when missing information.
    """,
    'depends': [
        'helpdesk_mrp',
    ],
    'data': [
        'view/helpdesk_ticket_view.xml',
        # 'view/mrp_workcenter_views.xml',
        'wizards/helpdesk_ticket_migrate_wizard.xml',
    ],
    'qweb': [],
    'installable': True,
    'auto_install': False,
}
