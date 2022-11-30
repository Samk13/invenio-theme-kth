"""Additional views."""
from flask import Blueprint
from flask_login import login_required
from invenio_app_rdm.records_ui.views.deposits import deposit_create, deposit_edit


@login_required
def guarded_deposit_create(*args, **kwargs):
    """Guard the creation page for records, based on permissions."""
    return deposit_create(*args, **kwargs)


@login_required
def guarded_deposit_edit(*args, **kwargs):
    """Guard the edit page for records, based on permissions."""
    return deposit_edit(*args, **kwargs)


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
        """Override the existing view functions with more access control."""
        app.view_functions[
            "invenio_app_rdm_records.deposit_edit"
        ] = guarded_deposit_edit
        app.view_functions[
            "invenio_app_rdm_records.deposit_create"
        ] = guarded_deposit_create

    return blueprint
