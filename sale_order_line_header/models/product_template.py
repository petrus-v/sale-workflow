# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class sale_order(osv.Model):
    # Private attributes
    _name = 'product.template'
    _inherit = 'product.template'

    # Fields declaration
    _columns = {
        'header_id': fields.many2one('sale.header', 'Default Header',
                                     help=u"This is default header that will be"
                                     u"used on sale order line.",
                                     required=False,)
    }

    # compute and search fields, in the same order that fields declaration
    # Constraints and onchanges
    # CRUD methods
    # Action methods
    # Business methods