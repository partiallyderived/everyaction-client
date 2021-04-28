# Need this so we can use source to activate virtual environment.
SHELL := /bin/bash

PACKAGE := everyaction
SPHINX_BUILD_DIR := docs
SPHINX_SOURCE_DIR := sphinx-source
VENV_DIR := venv
VENV_ACTIVATE := source $(VENV_DIR)/bin/activate

.PHONY: clean
clean: doc-clean
	rm -rf .pytest_cache

.PHONY: doc
doc: $(VENV_DIR)
	$(VENV_ACTIVATE) && sphinx-build -b html $(SPHINX_SOURCE_DIR) $(SPHINX_BUILD_DIR)

.PHONY: doc-clean
doc-clean:
	rm -rf $(SPHINX_SOURCE_DIR)/classes

.PHONY: doc-force
doc-force:
	$(VENV_ACTIVATE) && sphinx-build -b html -aE $(SPHINX_SOURCE_DIR) $(SPHINX_BUILD_DIR)

.PHONY: test
test: $(VENV_DIR)
	$(VENV_ACTIVATE) && python3 -m pytest -r sf

$(VENV_DIR): setup.py
	# Do not create new venv if it already exists, but delete it if it did not exist before and did not create without
	# error.
	([ -d $(VENV_DIR) ] || python3 -m venv $(VENV_DIR) || (rm -rf $(VENV_DIR) && false))
	$(VENV_ACTIVATE) && pip3 install -e .[doc,test] || (rm -rf $(VENV_DIR) && false)
	touch $(VENV_DIR)
	rm -rf everyaction_client.egg-info
