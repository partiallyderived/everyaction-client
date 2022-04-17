# Need this so we can use source to activate virtual environment.
SHELL := /bin/bash

PACKAGE := everyaction
SPHINX_BUILD_DIR := docs
SPHINX_SOURCE_DIR := docs-src
VENV_DIR := venv
VENV_ACTIVATE := source $(VENV_DIR)/bin/activate
VERSION_INC := patch

.PHONY: clean
clean:
	rm -rf .pytest_cache
	rm -rf $(SPHINX_SOURCE_DIR)/classes
	rm -rf $(SPHINX_BUILD_DIR)

.PHONY: doc
doc: $(VENV_DIR)
	rm -rf $(SPHINX_BUILD_DIR)/classes
	$(VENV_ACTIVATE) && sphinx-build -b html -aE $(SPHINX_SOURCE_DIR) $(SPHINX_BUILD_DIR)

.PHONY: linkcheck
linkcheck: $(VENV_DIR)
	$(VENV_ACTIVATE) && sphinx-build -b linkcheck $(SPHINX_SOURCE_DIR) $(SPHINX_BUILD_DIR)

.PHONY: publish
publish:
	git diff-index --quiet HEAD -- || (echo "Aborting: Uncommitted changes present" 1>&2 && false)
	git ls-files --other --directory --exclude-standard | sed q1 ||\
        (echo "Aborting: Untracked files present" 1>&2 && false)
	bash inc_version.sh $(VERSION_INC)
	VERSION=$$(sed -nE 's/version = (.*)/\1/p' setup.cfg);\
		git commit -a -m "Bump to version $$VERSION" &&\
		git tag -a "v$$VERSION" -m "Version $$VERSION" &&\
		git push --atomic origin main "v$$VERSION"

.PHONY: test
test: $(VENV_DIR)
	$(VENV_ACTIVATE) && python3 -m pytest -r sf -v everyaction/test

.PHONY: test-failed
test-failed: $(VENV_DIR)
	$(VENV_ACTIVATE) && python3 -m pytest -r sf -v --lf everyaction/test

$(VENV_DIR): setup.cfg
	# Do not create new venv if it already exists, but delete it if it did not exist before and did not create without
	# error.
	([ -d $(VENV_DIR) ] || python3 -m venv $(VENV_DIR) || (rm -rf $(VENV_DIR) && false))
	$(VENV_ACTIVATE) && python3 -m pip install -e .[doc,test] || (rm -rf $(VENV_DIR) && false)
	touch $(VENV_DIR)
	rm -rf everyaction_client.egg-info
