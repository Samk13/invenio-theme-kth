"""Invenio-Theme-KTH extension."""
from . import config
from .views import create_blueprint


class InvenioThemeKTH:
    """Invenio-Theme-KTH extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)
            self.blueprint = create_blueprint(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.extensions["invenio-theme-kth"] = self

    def init_config(self, app):
        """Initialize configuration."""
        # Use theme's base template if theme is installed
        for k in dir(config):
            app.config.setdefault(k, getattr(config, k))
