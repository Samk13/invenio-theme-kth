"""Additional views."""
from flask import Blueprint

from invenio_app_rdm.records_ui.views.deposits import (
    deposit_create,
    deposit_edit,
)

def create_blueprint(app):
    """Register blueprint routes on app."""
    blueprint = Blueprint(
        "invenio_theme_kth",
        __name__,
        template_folder="./templates",
        static_folder="static",
    )
    #
    # Views
    #
    @app.before_first_request
    def override_deposit_pages():
        app.view_functions["invenio_app_rdm_records.deposit_edit"] = deposit_edit
        app.view_functions["invenio_app_rdm_records.deposit_create"] = deposit_create

    return blueprint
