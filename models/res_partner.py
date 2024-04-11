# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    associated_products_ids = fields.Many2many(comodel_name="product.product", string="Associated Products")
