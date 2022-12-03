"""Additional views."""
from flask import Blueprint


def create_blueprint(app):
    """Register blueprint routes on app."""
    blueprint = Blueprint(
        "invenio_theme_kth",
        __name__,
        template_folder="./templates",
        static_folder="static",
    )

    return blueprint
