# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class sale_order_line_header(osv.Model):
    # Private attributes
    _name = 'sale.order.line.header'
    _description = 'Header to group sale order line'

    # Fields declaration
    _columns = {
        'name': fields.char(string='Header name', required=True,),
        'sequence': fields.integer('Sequence', required=True,
                                   help=u"Sequence to sort headers."),
        'header_id': fields.many2one('sale.header', 'Original header',
                                     required=False,),
        'sale_id': fields.many2one('sale.order', 'Sale order', required=True,),
        'sale_order_line_ids': fields.one2many('sale.order.line', 'header_id',
                                               u"Sale order line",),
    }

    # compute and search fields, in the same order that fields declaration
    # Constraints and onchanges
    # CRUD methods
    # Action methods
    # Business methods