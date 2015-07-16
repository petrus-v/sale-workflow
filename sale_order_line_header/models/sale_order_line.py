# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class sale_order_line(osv.Model):
    # Private attributes
    _name = 'sale.order.line'
    _inherit = 'sale.order.line'

    # Fields declaration
    _columns = {
        'header_id': fields.many2one('sale.order.line.header', 'Header',
                                     required=False,)
    }

    # compute and search fields, in the same order that fields declaration
    # Constraints and onchanges

    # CRUD methods
    # Action methods
    # Business methods