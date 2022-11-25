"""Additional views."""

from flask import Blueprint

# from flask import Blueprint, g, render_template
# from flask_login import current_user, login_required
# from invenio_app_rdm.records_ui.views.deposits import deposit_create, deposit_edit
# from invenio_rdm_records.proxies import current_rdm_records_service as rec_service


# Registration
#
# @login_required
# def guarded_deposit_create(*args, **kwargs):
#     """Guard the creation page for records, based on permissions."""
#     # if rec_service.check_permission(g.identity, "create"):
#     # return render_template(
#     #     "./semantic-ui/invenio_theme_kth/records/deposit.html", user=current_user
#     # )

#     return deposit_create(*args, **kwargs)


# @login_required
# def guarded_deposit_edit(*args, **kwargs):
#     """Guard the edit page for records, based on permissions."""
#     # NOTE: this extra loading of the draft introduces an extra DB query, but i think
#     #       it should not make too much of a difference for us
#     # draft = rec_service.draft_cls.pid.resolve(
#     #     kwargs["pid_value"], registered_only=False
#     # )
#     # if rec_service.check_permission(g.identity, "update_draft", record=draft):
#     # return render_template(
#     #     "./semantic-ui/invenio_theme_kth/records/deposit.html", user=current_user
#     # )

#     return deposit_edit(*args, **kwargs)


def create_blueprint(app):
    """Register blueprint routes on app."""
    blueprint = Blueprint(
        "invenio_theme_kth",
        __name__,
        template_folder="./templates",
    )
    #
    # Views
    #
    # @app.before_first_request
    # def override_deposit_pages():
    #     """Override the existing view functions with more access control."""
    #     app.view_functions[
    #         "invenio_app_rdm_records.deposit_edit"
    #     ] = guarded_deposit_edit
    #     app.view_functions[
    #         "invenio_app_rdm_records.deposit_create"
    #     ] = guarded_deposit_create

    return blueprint
