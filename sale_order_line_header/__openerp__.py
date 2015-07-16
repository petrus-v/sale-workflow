# -*- coding: utf-8 -*-
##############################################################################
#
#   sale_order_line_header for OpenERP
#   Copyright (C) 2015 Anybox Pierre Verkest <pverkest@anybox.fr>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Sale Payment Method',
    'version': '0.1.0',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'description': """
Sale order line header
======================

This module was written to extend the functionality of sort sale order lines
in your quotations.
""",
    'author': "Anybox, Odoo Community Association (OCA)",
    'website': 'http://anybox.fr/',
    'depends': [
        'sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product.xml',
        "views/sale_order.xml",
        'views/sale_header.xml',
        'views/menu.xml',
    ],
    'demo': [
        'demo/sale_header.xml',
        'demo/sale_order_line_header.xml',
    ],
    'installable': True,
}