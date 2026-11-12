# -*- coding: utf-8 -*-
{
    'name': 'InvoiceOne Identity Experience Login',
    'version': '15.0.1.0.0',
    'category': 'Website',
    'summary': 'Modern Split-Screen Corporate Login Experience with Dynamic Company NIF, License Status & Homologation Banner',
    'description': """
InvoiceOne Identity Experience Login
====================================
Transforms the default Odoo login screen into a modern, full-viewport split-screen corporate experience:
- Left Panel: Clean distraction-free authentication form, custom brand logo, dynamic company VAT/NIF, and real-time contract/license status indicator.
- Right Panel: Executive branding showcase with radial gradient background, dynamic company name header, AGT certification badge, and interactive value-pillars carousel.
- Homologation / Sandbox Mode: Built-in visual indicators (corner ribbon and top alert card) to clearly distinguish test/homologation environments from production.
- 100% compatible with Odoo 15.0, 16.0, 17.0, 18.0, 19.0 & 20.0 (Community & Enterprise).
    """,
    'author': 'DIGITALUB ANGOLA, LDA',
    'website': 'https://www.digitalub.ao',
    'support': 'suporte@digitalub.ao',
    'license': 'OPL-1',
    'price': 15.0,
    'currency': 'USD',
    'depends': ['web', 'portal'],
    'data': [
        'views/login_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'invoiceone_login/static/src/css/login_style.css',
        ],
    },
    'images': [
        'static/description/banner.png',
        'static/description/screenshot_prod.png',
        'static/description/screenshot_hml.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
