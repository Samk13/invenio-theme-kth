from . import config
from .views import create_blueprint


class InvenioThemeKTH:
    """Invenio-Theme-KTH extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        self.init_blueprint(app)
        app.extensions["invenio-theme-kth"] = self

    def init_blueprint(self, app):
        """Initialize blueprint."""
        self.blueprint = blueprint = create_blueprint(app)
        app.register_blueprint(blueprint)
        # since invenio-app-rdm currently (october 2022) doesn't offer an easy way of
        # overriding the provided jinja templates, we have to perform a workaround:
        # the first blueprint that has a definition for a template (per name) gets
        # selected by 'flask.render_template()' - thus, we just have to make sure that
        # our blueprint is inserted before the invenio_app_rdm blueprints
        #
        # this has to be done after everything (including *all* blueprints)
        # has been initialized, and is only really relevant for the UI
        # thus, we use `app.before_first_request` rather than a startup blueprint
        #
        # NOTE: the below code requires Flask 2.0.2+ and Python 3.7+
        #       for insertion-ordered dictionaries
        @app.before_first_request
        def register_kth_bp_first():
            bps = {
                name: bp
                for name, bp in app.blueprints.items()
                if name != "invenio_theme_kth"
            }

            app.blueprints = {"invenio_theme_kth": blueprint, **bps}

    def init_config(self, app):
        """Initialize configuration."""
        # Use theme's base template if theme is installed
        for k in dir(config):
            app.config.setdefault(k, getattr(config, k))
