# Copyright 2020 TechnoLibre <info@technolibre.ca>
# License AGPLv3.0 or later (https://www.gnu.org/licenses/agpl-3.0.en.html).

import logging
from odoo import _, fields, models, api
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class HelpdeskMergeCategoryWizard(models.TransientModel):
    _name = 'helpdesk.ticket.migrate.wizard'
    _description = "Migrate ticket in mrp phase 1"

    @api.model
    def default_get(self, fields):
        result = super(HelpdeskMergeCategoryWizard, self).default_get(fields)
        ticket_ids = self.env.context.get('active_ids', [])
        result["helpdesk_ticket_to_migrate"] = [(6, 0, ticket_ids)]
        return result

    helpdesk_ticket_to_migrate = fields.Many2many(
        comodel_name='helpdesk.ticket', required=True)

    # helpdesk_category_destination = fields.Many2one(
    #     comodel_name='helpdesk.ticket.category', required=True)
    #
    # send_emails = fields.Boolean(string="Send emails", default=False,
    #                              help="Send email for each ticket when change "
    #                                   "category.")

    def migrate_helpdesk_ticket_mrp_phase_1(self):
        if not self.helpdesk_ticket_to_migrate:
            raise UserError(_('Helpdesk ticket to migrate is empty.'))
        for ticket in self.helpdesk_ticket_to_migrate:
            ticket.migration_phase_1_mrp = "error"
            ticket.migration_phase_1_mrp_message = _("Cannot migrate for no reason.")
        # if not self.helpdesk_category_destination:
        #     raise UserError(_('Helpdesk category destination is empty.'))
        # # All ticket of category to merge will be transfer
        # lst_categories_to_merge = [a.id for a in self.helpdesk_categories_to_merge]
        # lst_ticket = self.env["helpdesk.ticket"].search(
        #     [('category_id', 'in', lst_categories_to_merge)])
        # for ticket in lst_ticket:
        #     ticket.with_context(mail_notrack=not self.send_emails).category_id = \
        #         self.helpdesk_category_destination.id
        #
        # self.env["helpdesk.ticket.category"].browse(
        #     lst_categories_to_merge).active = False
        pass
