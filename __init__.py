# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8
# =============================================================================
# $Id: __init__.py 45 2008-02-21 18:10:38Z s0undt3ch $
# =============================================================================
#             $URL: http://devnull.ufsoft.org/svn/GoogleAnalyticsWidget/trunk/__init__.py $
# $LastChangedDate: 2008-02-21 18:10:38 +0000 (Thu, 21 Feb 2008) $
#             $Rev: 45 $
#   $LastChangedBy: s0undt3ch $
# =============================================================================
# Copyright (C) 2007 Ufsoft.org - Pedro Algarvio <ufs@ufsoft.org>
#
# Please view LICENSE for additional licensing information.
# =============================================================================
# https://www.google.com/support/googleanalytics/bin/answer.py?answer=55585&topic=10981

from os.path import join, dirname
from textpress.widgets import Widget
from textpress.api import *

SHARED_FILES = join(dirname(__file__), 'shared')
TEMPLATES = join(dirname(__file__), 'templates')

class GoogleAnalyticsWidget(Widget):
    __metaclass__ = cache.make_metaclass(vary=('user',))
    NAME = 'get_google_analytics'
    TEMPLATE = 'google_analytics.html'

    def __init__(self, uid='', admin_logging=False, extensions='',
                 outbound_link_tracking=True, tracking_domain_name='',
                 google_external_path='/external/'):
        self.uid = uid
        self.admin_logging = admin_logging
        self.extensions = extensions
        self.outbound_link_tracking = outbound_link_tracking
        self.tracking_domain_name = tracking_domain_name
        self.google_external_path = google_external_path

    @staticmethod
    def get_display_name():
        return _('Google Analytics')

    @staticmethod
    def configure_widget(initial_args, request):
        args = form = initial_args.copy()
        error = None
        if request.method == 'POST':
            args['uid'] = request.form.get('uid', '')
            if not args['uid']:
                error = _("You need to enter your google analytics UUID")
            args['extensions'] = request.form.get('extensions', '')
            args['admin_logging'] = request.form.get('admin_logging') == 'yes'
            args['outbound_link_tracking'] = request.form.get('outbound_link_tracking') == 'yes'
            args['tracking_domain_name'] = request.form.get('tracking_domain_name', '')
            args['google_external_path'] = request.form.get('google_external_path', '')

        if error is not None:
            args = None
        return args, render_template('admin/google_analytics.html',
                                     error=error, form=form)


def setup(app, plugin):
    app.add_shared_exports('google_analytics', SHARED_FILES)
    app.add_template_searchpath(TEMPLATES)
    app.add_widget(GoogleAnalyticsWidget)
