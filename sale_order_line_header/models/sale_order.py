# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class sale_order(osv.Model):
    # Private attributes
    _name = 'sale.order'
    _inherit = 'sale.order'

    # Fields declaration
    _columns = {
        'header_ids': fields.one2many('sale.order.line.header', 'sale_id',
                                      'Headers', required=False,)
    }

    # compute and search fields, in the same order that fields declaration
    # Constraints and onchanges
    # CRUD methods
    # Action methods
    # Business methods