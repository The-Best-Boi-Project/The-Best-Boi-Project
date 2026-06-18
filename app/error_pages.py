from flask import Blueprint, render_template
from jinja2 import TemplateError

error_pages = Blueprint('error_pages', __name__)


@error_pages.app_errorhandler(404)
def not_found(_error):
    return render_template('errors/404.html.jinja'), 404


@error_pages.app_errorhandler(418)
def im_a_teapot(_error):
    return render_template('errors/418.html.jinja'), 418


@error_pages.app_errorhandler(500)
def internal_server_error(_error):
    return render_template('errors/500.html.jinja'), 500


@error_pages.app_errorhandler(TemplateError)
def template_not_found(error):
    return render_template('errors/500.html.jinja', error=error), 500
