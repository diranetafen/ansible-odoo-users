import sys
import odoorpc

odoo = odoorpc.ODOO('localhost', port=80)
timeout_backup = odoo.config['timeoutt']
odoo.config['timeout'] = 240
odoo.db.create('admin', 'test_db' , false, 'fr_FR', 'password')
odoo.config['timeout'] = timeout_backup
