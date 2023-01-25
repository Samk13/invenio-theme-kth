# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-config-kth is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.
from .utils.registration_form import kth_registration_form

# Invenio-Theme
"""Invenio-Theme config."""
# =============
# See https://invenio-theme.readthedocs.io/en/latest/configuration.html


APP_THEME = ["semantic-ui"]
"""The application theme to use."""


APP_RDM_DEPOSIT_FORM_TEMPLATE = "invenio_app_rdm/records/deposit_override.html"
"""Deposit form page template override."""

TERMS_OF_USE_TEXT = "I confirm that I have read and fully understand the \
<a class='pull-right' href='https://www.kth.se/social/terms/' target='_blank'>terms and conditions</a> \
of KTH Royal Institute of Technology."
"""Signup terms and agreement Checkbox label text"""

OAUTHCLIENT_SIGNUP_FORM = kth_registration_form
"""user registration terms of use checkbox."""
