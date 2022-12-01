# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-config-kth is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

"""Additional views."""
from flask import Blueprint, render_template
from flask_login import login_required
from invenio_app_rdm.records_ui.views.decorators import (
    pass_draft,
    pass_draft_community,
    pass_draft_files,
)
from invenio_app_rdm.records_ui.views.deposits import (
    get_form_config,
    get_search_url,
    new_record,
)
from invenio_rdm_records.resources.serializers import UIJSONSerializer


@login_required
@pass_draft_community
def deposit_create_override(community=None):
    """Create a new deposit."""
    return render_template(
        "invenio_app_rdm/records/deposit_override.html",
        forms_config=get_form_config(createUrl="/api/records"),
        searchbar_config=dict(searchUrl=get_search_url()),
        record=new_record(),
        files=dict(default_preview=None, entries=[], links={}),
        preselectedCommunity=community,
    )


@login_required
@pass_draft(expand=True)
@pass_draft_files
def deposit_edit_override(pid_value, draft=None, draft_files=None):
    """Edit an existing deposit."""
    files_dict = None if draft_files is None else draft_files.to_dict()
    ui_serializer = UIJSONSerializer()
    record = ui_serializer.dump_obj(draft.to_dict())

    return render_template(
        "invenio_app_rdm/records/deposit_override.html",
        forms_config=get_form_config(apiUrl=f"/api/records/{pid_value}/draft"),
        record=record,
        files=files_dict,
        searchbar_config=dict(searchUrl=get_search_url()),
        permissions=draft.has_permissions_to(["new_version", "delete_draft"]),
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
        """Override the existing view functions with more access control."""
        app.view_functions[
            "invenio_app_rdm_records.deposit_edit"
        ] = deposit_edit_override
        app.view_functions[
            "invenio_app_rdm_records.deposit_create"
        ] = deposit_create_override

    return blueprint
