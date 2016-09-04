# -*- coding: utf-8 -*-
# Copyright (C) 2016-Today: La Louve (<http://www.lalouve.net/>)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


{
    'name': 'Capital Souscription',
    'version': '9.0.0.0.0',
    'category': 'Accounting',
    'summary': 'Provide extra accounting features for capital souscription',
    'author': 'La Louve',
    'website': 'http://www.lalouve.net',
    'depends': [
        'account',
    ],
    'data': [
        'views/view_capital_fundraising_wizard.xml',
        'views/view_product_template.xml',
        'views/view_res_partner.xml',
        'views/view_account_invoice.xml',
        'views/view_account_journal.xml',
        'views/view_capital_fundraising_type.xml',
        'views/view_capital_fundraising_category.xml',
        'views/view_capital_fundraising.xml',
        'views/view_account_payment_term.xml',
        'views/action.xml',
        'views/menu.xml',
    ],
    'demo': [
        'demo/res_groups.xml',
        'demo/account_payment_term.xml',
        'demo/account_account.xml',
        'demo/account_journal.xml',
        'demo/product_category.xml',
        'demo/product_product.xml',
        'demo/capital_fundraising.xml',
        'demo/capital_fundraising_type.xml',
        'demo/capital_fundraising_category.xml',
        'demo/capital_fundraising_category_line.xml',
        'demo/res_partner.xml',
    ],
    'installable': True,
}
