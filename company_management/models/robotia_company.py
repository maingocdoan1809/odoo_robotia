# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.addons.company_management.common import message
from odoo.addons.phone_validation.tools.phone_validation import phone_parse
from odoo.addons.web.controllers import utils
class Company(models.Model):
    _name = 'robotia.company'
    _description = 'Company'
    partner_id = fields.Many2one('res.partner', string='Partner', ondelete='restrict', auto_join=True, index=True, delegate=True)
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)
    charter_capital = fields.Monetary("Charter Capital", currency_field="currency_id")

    @api.constrains('phone')
    def validate_phone(self):
        for record in self:
            try:
                phone_parse(record.phone, record.country_id.code)
            except:
                raise ValidationError(message.PHONE_INVALID_ERR)

    @api.model
    def get_default_dashboard_search_view_id(self):
        return self.env.ref('company_management.robotia_company_view_search').id

    @api.model
    def get_default_dashboard_company(self):
        record = self.env.ref("company_management.robotia_company")
        action_id = self.env.ref("company_management.robotia_company_action").read()[0]
        action_data = utils.clean_action(action_id, self.env)
        return {
            **action_data,
            "res_id": record.id,
            "binding_view_types": ["form"],
            "view_mode": "form",
            "views": [[False, 'form']],
        }
