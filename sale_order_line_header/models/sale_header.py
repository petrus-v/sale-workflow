# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class sale_header(osv.Model):
    # Private attributes
    _name = 'sale.header'
    _description = u"""Default sale order line header"""

    # Fields declaration
    _columns = {
        'name': fields.char(string='Default header name', required=True,),
        'sequence': fields.integer('Default sequence', required=True,
                                   help=u"Default sequence to sort headers."),
        'product_ids': fields.one2many('product.template', 'header_id',
                                       u"Products")
    }

    # compute and search fields, in the same order that fields declaration
    # Constraints and onchanges
    # CRUD methods
    # Action methods
    # Business methods