# -*- coding: utf-8 -*-
from appdirs import unicode
from odoo import models, fields, api, _, tools

# class ProjectTask(models.Model):
#     _inherit = "project.task"
#     _description = "project cust"
from odoo.addons.web.doc.conf import project


class ProjectProject(models.Model):

    _inherit = "project.project"
    _description = "project cust"


    # ajout champs amount_market dans le modele facturation
    moy_pourcentage = fields.Float(string='pourcentage avancement', compute='_get_pourcentage_avancemant')
    # advance = fields.Boolean(string="% site section", compute='_get_per_advance_categ', default=False)

    # @api.depends('partner_id', 'state')
    def _get_pourcentage_avancemant(self):
        """
        Calculer Montant Marché par client.
        """

        prjt_ids = self.env['project.task'].search([('partner_id', '=', self.partner_id.id)])
        pourcentage = 0.0
        for par in prjt_ids:
            pourcentage += par.x_studio_pourcentage_davancement

        self.moy_pourcentage = pourcentage*100


    # @api.depends('invoice_line_ids.x_studio_pourcentage_situation')
    # def _get_per_advance_categ(self):
    #     """
    #     Calculer advance.
    #     """
    #     # *********************************
    #     for rec in self:
    #
    #         rec.advance = False
    #         av_line = 0.0
    #         comp_line = 0
    #         av_section = 0.0
    #         comp_section = 0
    #         # av_note = 0.0
    #
    #         for line in reversed(rec.invoice_line_ids):
    #
    #             if line.display_type != 'line_section' and line.display_type != 'line_note':
    #                 # av_line += line.per_advance_product
    #                 av_line += line.x_studio_pourcentage_situation
    #                 comp_line += 1
    #             if line.display_type == 'line_section':
    #                 if comp_line != 0:
    #                     av_section += av_line
    #                     av_line -= av_line
    #                     comp_line = 0
    #                     comp_section += 1
    #
    #             if line.display_type == 'line_note':
    #                 if comp_section != 0:
    #                     av_note = av_section
    #                     av_section -= av_section
    #                     comp_section = 0
    #                     line.x_studio_pourcentage_situation = av_note
    #                     # line.write({'per_advance_note': av_note
    #                     #             })
    #
    #         rec.advance = True


# class AccountMoveLine(models.Model):
#     _inherit = "account.move.line"
#     _description = "Journal Item"
#
#     # per_advance_note = fields.Float(string="% note", )
#     categ_id = fields.Many2one(related="product_id.categ_id")
