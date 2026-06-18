from flask import Blueprint, abort, render_template
from jinja2.exceptions import TemplateNotFound

content = Blueprint('content', __name__)


@content.route('/models')
def models():
    return render_template('models.html.jinja')


# @content.route('/clothing')
# def clothing():
#     return render_template('clothing.html.jinja')


@content.route('/worlds')
def worlds():
    return render_template('worlds.html.jinja')


@content.route('/avatars/<avatar_type>')
def avatar(avatar_type: str):
    try:
        return render_template(f'avatars/avatar-{avatar_type}.html.jinja')
    except TemplateNotFound:
        abort(404)
