# -*- coding: utf-8 -*-
from appdirs import unicode
from odoo import models, fields, api, _, tools


class AccountMove(models.Model):
    _inherit = "account.move"
    _description = "Journal Entry"

    # ajout champs amount_market dans le modele facturation
    amount_market = fields.Monetary(string='Montant Marché', compute='_get_amount_market_sale')
    # @api.depends('partner_id', 'state')
    def _get_amount_market_sale(self):
        """
        Calculer Montant Marché par client.
        """
        sale_ids = self.env['sale.order'].search([('partner_id', '=', self.partner_id.id), ('state', '=', 'sale')])
        amount = 0.0
        for par in sale_ids:
            amount += par.amount_total

        self.amount_market = amount



    @api.depends('invoice_line_ids.x_studio_subtotal')
    def _get_per_advance_categ_subtot(self):
        """
        Calculer advance.
        """
        # *********************************
        for rec in self:

            rec.advance = False
            av_line = 0.0
            comp_line = 0
            av_section = 0.0
            comp_section = 0
            # av_note = 0.0

            for line in reversed(rec.invoice_line_ids):

                if line.display_type != 'line_section' and line.display_type != 'line_note':
                    # av_line += line.per_advance_product
                    av_line += line.x_studio_subtotal
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
                        line.x_studio_subtotal = av_note
                        # line.write({'per_advance_note': av_note
                        #             })

            rec.advance = True


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"
    _description = "Journal Item"

    # per_advance_note = fields.Float(string="% note", )
    categ_id = fields.Many2one(related="product_id.categ_id")
