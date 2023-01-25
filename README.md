# invenio-theme-kth
This module provides templates overrides and modification to invenio default theme:
- Customization of templates and modifications to the Invenio default theme are provided by this module
- Addeding a check box to the registration process when using third-party authentication services such as ORCID to ensure agreement with the terms of use before registration.

## Installation
```bash
pip install invenio-theme-kth
```

## Components
`views.py`: provides a Blueprint that registers both the static/ and templates/ folders to be usable by Invenio

`webpack.py`: registers the front-end assets (in the assets/ folder) to webpack

`config.py`: overrides several configuration items related to theming Invenio If new files is been added, first run:

## Development
This section intended if you want to further develop this module.
## Local setup
```bash
make install
# if you use pyenv
make install-pipenv
make test
```

while working on assets you can watch the assets with
```bash
invenio-cli assets watch
```
When you are done with your development
```bash
invenio-cli assets build
```

## Upload to pypi
make package-create # this will zip the package into dist dir
make package-check # verify if the package pass twine checks
twine upload -u <USERNAME> -p <PASSWORD> --repository-url https://test.pypi.org/legacy/ dist/* --verbose