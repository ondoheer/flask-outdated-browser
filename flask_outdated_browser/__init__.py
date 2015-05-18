# -*- coding: utf-8 -*-
"""
    flaskext.outdated-browser
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Adds outdatedbrowser easily to any flask project

    :copyright: (c) 2015 by ondoheer.
    :license: MIT, see LICENSE for more details.
"""

__version__ = '0.1'
__version_info__ = __version__.split('.')
__author__ = 'Pedro Baumann'
__license__ = 'MIT'
__copyright__ = '(c) 2015 - Pedro Baumann.'

from flask import Blueprint


class OutdatedBrowser(object):
    """
    :param: app: Flask aplication

    """

    def __init__(self, app=None):

        if app:
            self.init_app(app)

    def init_app(self, app):

        self.app = app

        app.config.setdefault('OUTDATED_BROWSER_FOR', "IE10")
        app.config.setdefault('OUTDATED_BROWSER_JQUERY', False)
        app.config.setdefault('OUTDATED_BROWSER_AJAX', False)
        app.config.setdefault('OUTDATED_BROWSER_MINIFIED', True)
        app.config.setdefault('OUTDATED_BROWSER_LANGUAGE', 'en')

        blueprint = Blueprint(
            'outdated', __name__,
            static_folder='static',
            template_folder='templates',
            static_url_path=app.static_url_path + '/outdated', )

        app.register_blueprint(blueprint)

        if not hasattr(app, 'extensions'):
            app.extensions = {}
