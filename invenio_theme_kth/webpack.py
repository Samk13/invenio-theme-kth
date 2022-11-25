"""JS/CSS Webpack bundles for invenio-theme-kth."""

from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    "assets",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "invenio-app-rdm-deposit-override": "./js/invenio_theme_kth/deposit/index.js",
            },
            aliases={
                "@js/invenio_theme_kth": "js/invenio_theme_kth",
            },
        ),
    },
)
