# -*- coding: utf-8 -*-
{
    'name': 'All in One Cheque',
    'version': '1.0',
    'summary': 'Print  Checks',
    'description': """
This module allows to print your payments on pre-printed checks.
You can configure the output (layout, stubs, paper format, etc.) in company settings, and manage the
checks numbering (if you use pre-printed checks without numbers) in journal settings.
As per Canadian Payment Association (https://www.payments.ca/sites/default/files/standard_006_complete_0.pdf)
 jku8
Supported formats
-----------------
- Check on top : Quicken / QuickBooks standard
- Check on middle: Peachtree standard
- Check on bottom: ADP standard
    """,
    'website': 'https://www.odoo.com/app/accounting',
    'depends': ['account_check_printing'],
    'data': [
        'data/all_in_one.xml',
        'report/print_check.xml',
        'report/print_check_top.xml',
        'report/print_check_middle.xml',
        'report/print_check_bottom.xml',
        'report/blank.xml',
        'views/cheque_form.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,

}
