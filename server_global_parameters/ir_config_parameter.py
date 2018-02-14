# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models
import odoo.tools as tools


class ir_config_parameter(models.Model):
    _inherit = 'ir.config_parameter'

    def get_param(self, cr, uid, key, default=False, context=None):
        """
        """
        if not self.search(
                cr, uid, [('key', '=', key)], context=context) and not default:
            server_value = tools.config.get(key)
            if server_value:
                return str(server_value)
        return super(ir_config_parameter, self).get_param(
            cr, uid, key, default=default, context=context)
