from flask import Flask

from .content import content
from .core import core
from .error_pages import error_pages
from .i18n import babel, get_locale


def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(content)
    app.register_blueprint(core)
    app.register_blueprint(error_pages)

    babel.init_app(app, locale_selector=get_locale)

    return app
