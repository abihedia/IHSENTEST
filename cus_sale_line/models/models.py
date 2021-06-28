# -*- coding: utf-8 -*-
from appdirs import unicode
from odoo import models, fields, api, _, tools

class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "Sale order"

    # ajout champs amount_market dans le modele facturation

    advance_bc = fields.Boolean(string="subtotal section", compute='_get_per_advance_categ_subtot_bc', default=False)


    @api.depends('order_line.price_subtotal')
    def _get_per_advance_categ_subtot_bc(self):
        """
        Calculer total_note.
        """
        # *********************************
        for rec in self:

            rec.advance_bc = False
            av_line = 0.0
            comp_line = 0
            av_section = 0.0
            comp_section = 0
            # av_note = 0.0

            for line in reversed(rec.order_line):

                if line.display_type != 'line_section' and line.display_type != 'line_note':
                    # av_line += line.per_advance_product
                    av_line += line.price_subtotal
                    comp_line += 1
                if line.display_type == 'line_section':
                    if comp_line != 0:
                        av_section += av_line
                        av_line -= av_line
                        comp_line = 0
                        comp_section += 1

                if line.display_type == 'line_note':
                    if comp_section != 0:
                        av_note = av_section
                        av_section -= av_section
                        comp_section = 0
                        line.price_subtotal = av_note
                        # line.write({'per_advance_note': av_note
                        #             })

            rec.advance_bc = True


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    _description = "Journal Item Sale order line"




    # per_advance_note = fields.Float(string="% note", )
    categ_id = fields.Many2one(related="product_id.categ_id")
