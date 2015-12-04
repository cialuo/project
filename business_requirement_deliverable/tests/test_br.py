# -*- coding: utf-8 -*-
# © 2015
# Elico Corp, contributor: Eric Caudal, Alex Duan, Xie XiaoPeng
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp.tests import common


@common.at_install(False)
@common.post_install(True)
class BusinessRequirementTestCase(common.TransactionCase):
    def setUp(self):
        super(BusinessRequirementTestCase, self).setUp()
        self.br = self.env['business.requirement']

    def test_get_resource_time_total(self):
        vals = {
            'name': ' test',
            'deliverable_lines': [
                (0, 0, {'description': 'line1', 'resource_time': 15.0}),
                (0, 0, {'description': 'line2', 'resource_time': 25.0}),
                (0, 0, {'description': 'line3', 'resource_time': 35.0}),
                (0, 0, {'description': 'line4', 'resource_time': 45.0}),
            ]
        }
        br = self.br.create(vals)
        br._get_resource_time_total()
        time_total = br.resource_time_total
        self.assertEqual(time_total, 15.0 + 25.0 + 35.0 + 45.0)