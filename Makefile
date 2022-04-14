# Need this so we can use source to activate virtual environment.
SHELL := /bin/bash

PACKAGE := everyaction
SPHINX_BUILD_DIR := docs
SPHINX_SOURCE_DIR := docs-src
VENV_DIR := venv
VENV_ACTIVATE := source $(VENV_DIR)/bin/activate
VERSION := $(shell sed -nE 's/version = (.*)/\1/p' setup.cfg)

.PHONY: clean
clean:
	rm -rf .pytest_cache
	rm -rf $(SPHINX_SOURCE_DIR)/classes
	rm -rf docs/.buildinfo

.PHONY: doc
doc: $(VENV_DIR)
	rm -rf $(SPHINX_BUILD_DIR)/classes
	$(VENV_ACTIVATE) && sphinx-build -b html -aE $(SPHINX_SOURCE_DIR) $(SPHINX_BUILD_DIR)
	git add $(SPHINX_BUILD_DIR)

.PHONY: inc
inc:
	bash inc_version.sh

.PHONY: linkcheck
linkcheck: $(VENV_DIR)
	$(VENV_ACTIVATE) && sphinx-build -b linkcheck $(SPHINX_SOURCE_DIR) $(SPHINX_BUILD_DIR)

.PHONY: tag
tag:
	git tag -a v$(VERSION) -m "Version $(VERSION)"

.PHONY: test
test: $(VENV_DIR)
	$(VENV_ACTIVATE) && python3 -m pytest -r sf -v

.PHONY: test-failed
test-failed: $(VENV_DIR)
	$(VENV_ACTIVATE) && python3 -m pytest -r sf -v --lf

$(VENV_DIR): setup.cfg
	# Do not create new venv if it already exists, but delete it if it did not exist before and did not create without
	# error.
	([ -d $(VENV_DIR) ] || python3 -m venv $(VENV_DIR) || (rm -rf $(VENV_DIR) && false))
	$(VENV_ACTIVATE) && python3 -m pip install -e .[doc,test] || (rm -rf $(VENV_DIR) && false)
	touch $(VENV_DIR)
	rm -rf everyaction_client.egg-info
