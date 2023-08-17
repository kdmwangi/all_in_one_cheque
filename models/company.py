# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class Company(models.Model):
    _inherit = "res.company"

    # here, key has to be full xmlID(including the module name) of all the
    # new report actions that you have defined for check layout
    account_check_printing_layout = fields.Selection(selection_add=[
        ('all_in_one_cheque.action_print_check_top', 'Print Check (Top) - CA'),
        ('all_in_one_cheque.action_print_check_middle', 'Print Check (Middle) - CA'),
        ('all_in_one_cheque.action_print_check_bottom', 'Print Check (Bottom) - CA'),
        ('all_in_one_cheque.action_print_blank', 'Print blank (Bottom) - CA'),
    ], ondelete={
        'all_in_one_cheque.action_print_check_top': 'set default',
        'all_in_one_cheque.action_print_check_middle': 'set default',
        'all_in_one_cheque.action_print_check_bottom': 'set default',
        'all_in_one_cheque.action_print_blank': 'set default',
    })
