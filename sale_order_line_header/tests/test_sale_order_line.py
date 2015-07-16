# -*- coding: utf-8 -*-
from openerp.tests import common


class TestSaleOrderLine(common.TransactionCase):

    def setUp(self):
        super(TestSaleOrderLine, self).setUp()
        self.sale_order = self.registry('sale.order')
        self.sale_order_line = self.registry('sale.order')
        self.order_id = self.sale_order.create(self.cr, self.uid,
                                             {'partner_id': self.ref(
                                                 'base.res_partner_15'),
                                              'pricelist_id': self.ref(
                                                     'product.list0'),
                                              'partner_invoice_id': self.ref(
                                                 'base.res_partner_15'),
                                              'partner_shipping_id': self.ref(
                                                 'base.res_partner_15'),
                                             })

    def create_sol(self, product_id, devis_id):
        """When creating a sale order line, main features are set through
        the onchange method"""
        cr, uid = self.cr, self.uid
        sol_id = self.order_line.create(
            cr, uid, {'product_id': product_id,
                      'name': "test product",
                      'order_id': devis_id})
        sol = self.sale_order_line.browse(cr, uid, sol_id)
        result = self.sale_order_line.product_id_change(
            cr, uid, [sol.id],
            sol.order_id.pricelist_id.id,
            product_id,
            partner_id=sol.partner_id.id)
        self.order_line.write(cr, uid, [sol.id], result['value'])
        return sol.id

    def test_add_first_sale_order_line(self):
        """Adding a sale order line, on empty sale order should add a
        sale_order_line_header"""
        self.create_sol(self.ref('base.product_product_44'), self.order_id)
        self.assertFalse(True)
