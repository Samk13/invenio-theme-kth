.DEFAULT_GOAL=ls

ls: # List available commands
	@grep '^[^#[:space:]].*:' Makefile

format: # Black format and isort imports
	@black . && isort .

install: # Install py dependencies
	@pip install -e ".[tests, opensearch2]"

install-pipenv: # Install py dependencies using pipenv
	@pipenv install -e ".[tests]"

test: # Run tests
	@bash run-tests.sh

# Packagin
package-create: # Package to tar.gz file for uploading to pypi
	@python setup.py sdist

package-check: # Check package if it pass pypi tests
	@twine check dist/*