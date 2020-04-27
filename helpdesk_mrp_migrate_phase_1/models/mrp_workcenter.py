# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, exceptions, fields, models, _


class MrpWorkcenter(models.Model):
    _inherit = 'mrp.workcenter'

    helpdesk_id = fields.Many2one(comodel_name="helpdesk.ticket",
                                  string="Helpdesk ticket")
    is_approved = fields.Boolean(string="Is approved", default=False)
    last_partner_approval = fields.Many2one(string="Last user approval",
                                            compute="_user_is_approved",
                                            comodel_name="res.users")

    @api.multi
    @api.depends('is_approved')
    def _user_is_approved(self):
        if self.is_approved:
            self.last_partner_approval = self.env.user
        else:
            self.last_partner_approval = False
