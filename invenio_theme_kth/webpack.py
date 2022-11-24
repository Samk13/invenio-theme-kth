"""JS/CSS Webpack bundles for invenio-theme-kth."""

from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    "assets",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "my-component": "./assets/semantic-ui/js/invenio_theme_kth/MyComponent.js"
            },
        ),
    },
)
