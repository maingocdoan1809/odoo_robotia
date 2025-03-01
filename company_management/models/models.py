# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.addons.company_management.common import message
class Company(models.Model):
    _name = 'robotia.company'
    _description = 'Company'
    partner_id = fields.Many2one('res.partner', string='Partner', ondelete='restrict', auto_join=True, index=True, delegate=True)
    charter_capital = fields.Char('Charter Capital')

    @api.constrains('phone')
    def validate_phone(self):
        for record in self:
            try:
                record._phone_format(raise_exception=True)
            except:
                raise ValidationError(message.PHONE_INVALID_ERR)

