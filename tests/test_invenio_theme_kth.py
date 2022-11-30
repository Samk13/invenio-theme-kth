# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-config-kth is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.
from flask import Flask

from invenio_theme_kth import InvenioThemeKTH, __version__


def test_version():
    """Test version import."""
    from invenio_theme_kth import __version__

    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask("testapp")
    ext = InvenioThemeKTH(app)
    assert "InvenioThemeKTH" not in app.extensions
    ext.init_app(app)
    assert "invenio-theme-kth" in app.extensions
