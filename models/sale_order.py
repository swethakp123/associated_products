# -*- coding: utf-8 -*-
from odoo import models, fields, api, Command


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    associated_product = fields.Boolean(string='associated_product', compute="_compute_associated_product",
                                        readonly=False)

    @api.onchange('partner_id', 'associated_product')
    def _compute_associated_product(self):
        order_line_values = []

        if self.partner_id and self.associated_product:
            associated_products = self.partner_id.associated_products_ids

            for associated_product in associated_products:
                matching_line = self.order_line.filtered(lambda rec: rec.product_id.id == associated_product.id)
                if matching_line:
                    matching_line.product_uom_qty += 1
                else:
                    order_line_values.append((Command.create({
                        'product_id': associated_product.id,
                        'name': associated_product.name,
                        'product_uom_qty': 1,
                        'product_uom': associated_product.uom_id.id,
                        'price_unit': associated_product.list_price
                    })))
        elif self.partner_id and not self.associated_product:
            associated_products = self.partner_id.associated_products_ids
            for product in associated_products:
                for line in self.order_line.filtered(lambda x: x.product_id == product):
                    order_line_values.append((Command.update(line.id,
                                                             {'product_uom_qty': line.product_uom_qty - 1})))
                    if line.product_uom_qty <= 1:
                        order_line_values.append((Command.unlink(line.id)))

        self.order_line = order_line_values

