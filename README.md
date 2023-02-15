# invenio-theme-kth
This module provides templates overrides and modification to invenio default theme:
- Customization of templates and modifications to the Invenio default theme are provided by this module
- Adding terms of use check box to the registration process when using third-party authentication services such as ORCID before registration.

## Installation
```bash
pip install invenio-theme-kth
```

## Components
`views.py`: provides a Blueprint that registers both the static/ and templates/ folders to be usable by Invenio

`webpack.py`: registers the front-end assets (in the assets/ folder) to webpack

`config.py`: overrides several configuration items related to theming Invenio If new files is been added, first run:

## Maintainers
This section intended for you who want to further develop this module.

### Last Updated
> invenio RDM V11

### Maintaining
Keep the following files up to date with source:

[RDMDepositFormOverride.js](invenio_theme_kth/assets/semantic-ui/js/invenio_theme_kth/deposit/RDMDepositFormOverride.js) with
[Source RDMDepositForm.js](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/theme/assets/semantic-ui/js/invenio_app_rdm/deposit/RDMDepositForm.js)

[index.js](invenio_theme_kth/assets/semantic-ui/js/invenio_theme_kth/deposit/index.js) with [Source index.js](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/theme/assets/semantic-ui/js/invenio_app_rdm/deposit/index.js)

Update translations:
[Follow the steps here](.tx/config)

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

```console
make package-create
make package-upload USER="" PASS=""
```

- make package-create # it Will:
1. remove old dist folder
2. auto increment package version
3. zip the package into dist dir
4. check if the package pass twin checks

> you can change version increment to major or minor by adding args:
> -ma -> major increment `make package-create ARG="-ma"`

> -mi -> minor increment `make package-create ARG="-mi"`

> -pa -> patch increment you can leave it blank as default `make package-create`

- make package-check # verify if the package pass twine checks

- make package-upload USER="" PASS="" # will  and upload to pypi will prompt for username and pass

or manually:
twine upload -u <USERNAME> -p <PASSWORD> dist/* --verbose