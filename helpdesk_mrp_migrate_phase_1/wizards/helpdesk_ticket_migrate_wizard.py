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

    select_all_tickets = fields.Boolean(string="Select all tickets", default=False,
                                        help="Migrate all active tickets.")

    def migrate_helpdesk_ticket_mrp_phase_1(self):
        if not self.helpdesk_ticket_to_migrate:
            raise UserError(_('Helpdesk ticket to migrate is empty.'))
        i = 0

        if self.select_all_tickets:
            category_id = self.env.ref(
                'helpdesk_supplier.helpdesk_ticket_category_supplier_applicant').id
            tickets = self.env["helpdesk.ticket"].search(
                [('category_id', '=', category_id)])
        else:
            tickets = self.helpdesk_ticket_to_migrate

        i_max = len(tickets)
        for ticket in tickets:
            i += 1
            print(f"{i}/{i_max} migration")
            self._migrate_ticket(ticket)

    def _migrate_ticket(self, ticket):
        region = ""
        company_name = ""
        other_machine_available = ""
        type_of_service = ""
        printer_dimension = ""
        available_material = ""
        other_available_material = ""
        available_machine = ""
        key_company = "Compagnie / Société (à mentionner si les ressources de la " \
                      "compagnie sont utilisées)"
        key_company_2 = 'Compagnie (à mentionner si les ressources de la compagnie ' \
                        'sont utilisées)'
        key_company_3 = 'Compagnie'
        key_type_of_service = "Type de services"
        key_other_machine_available = 'Autres machine(s) disponible(s)'
        key_printer_dimension = 'Dimension des imprimantes 3D'
        key_available_material = 'Matériaux disponibles d\'impression 3D'
        key_other_available_material = 'Autres matériaux disponibles'
        key_available_machine = 'Machine(s) disponible(s)'
        key_available_machine_2 = 'Machine(s) disponible'
        key = "Custom infos\n___________\n\n"

        last_key = None

        min_index = ticket.description.find(key)
        max_index = min_index + len(key)
        split_info = ticket.description[max_index:-5].strip().split("\n")

        # Get administrative region
        if min_index:
            region = ticket.description[3:min_index].strip()

        for info in split_info:
            split_key = " : "
            if split_key not in info:
                # Accumulate data with textarea fields
                if last_key == key_printer_dimension:
                    printer_dimension += f"\n{info}"
                elif last_key == key_other_machine_available:
                    other_machine_available += f"\n{info}"
                else:
                    ticket.migration_phase_1_mrp = "error"
                    ticket.migration_phase_1_mrp_message = _(
                        "Cannot parse key value in custom infos '%s'.") % info
                    return
                continue

            if "</p><p>" in info:
                ticket.migration_phase_1_mrp = "error"
                ticket.migration_phase_1_mrp_message = _(
                    "Cannot parse description.")
                return

            key, value = info.split(" : ")

            if key_company == key or key_company_2 == key or key_company_3 == key:
                # Validate company of the partner_id is right
                if not ticket.partner_id:
                    if ticket.ignore_missing_company:
                        continue
                    ticket.migration_phase_1_mrp = "warning"
                    ticket.migration_phase_1_mrp_message = _(
                        "Create partner_id.")
                    return
                if not ticket.partner_id.parent_id:
                    if ticket.ignore_missing_company:
                        continue
                    ticket.migration_phase_1_mrp = "warning"
                    ticket.migration_phase_1_mrp_message = _(
                        "Configure company '%s' to partner_id.") % value
                    return
                company_name = value
            elif key_other_machine_available == key:
                other_machine_available = value
                key_other_machine_available = key
            elif key_type_of_service == key:
                type_of_service = value
            elif key_printer_dimension == key:
                printer_dimension = value
                last_key = key
            elif key_available_material == key:
                available_material = value
            elif key_other_available_material == key:
                other_available_material = value
            elif key_available_machine == key or key_available_machine_2 == key:
                available_machine = value
            else:
                ticket.migration_phase_1_mrp = "error"
                ticket.migration_phase_1_mrp_message = _(
                    "Unknown key/value : %s/%s") % (key, value)

        ticket.migration_phase_1_mrp = "success"
        ticket.migration_phase_1_mrp_message = ""

        # Validate minimum information to finish migration
        if not company_name and not ticket.ignore_missing_company:
            ticket.migration_phase_1_mrp = "warning"
            ticket.migration_phase_1_mrp_message = _("Missing company information")

        if not type_of_service:
            ticket.migration_phase_1_mrp = "warning"
            ticket.migration_phase_1_mrp_message = _(
                "Missing type of service information")

        if not printer_dimension:
            ticket.migration_phase_1_mrp = "warning"
            ticket.migration_phase_1_mrp_message = _(
                "Missing printer dimension")

        # if not available_material:
        #     ticket.migration_phase_1_mrp = "warning"
        #     ticket.migration_phase_1_mrp_message = _(
        #         "Missing available material")

        # if not available_machine:
        #     ticket.migration_phase_1_mrp = "warning"
        #     ticket.migration_phase_1_mrp_message = _(
        #         "Missing available machine")

        if ticket.partner_name:
            ticket.name = f"{ticket.partner_name} ({len(type_of_service.split(','))})"

        return region, company_name, type_of_service, printer_dimension, \
               available_material, other_available_material, other_machine_available, \
               available_machine
