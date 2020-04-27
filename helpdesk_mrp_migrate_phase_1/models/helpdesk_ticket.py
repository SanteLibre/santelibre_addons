from odoo import _, api, fields, models, tools
from odoo.exceptions import UserError


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    migration_phase_1_mrp = fields.Selection(selection=[
        ('none', _('No migrate')),
        ('success', _('Success')),
        ('warning', _('Warning')),
        ('error', _('Error')),
    ], string='Migration status phase 1 mrp', default='none',
        track_visibility='onchange',
    )

    migration_phase_1_mrp_message = fields.Char(
        string="Migration message phase 1 mrp",
        track_visibility='onchange',
        help="Help to diagnostic the migration.",
    )
