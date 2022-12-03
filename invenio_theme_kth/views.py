# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-config-kth is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

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
