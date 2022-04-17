# Python Client for EveryAction

This is the developer documentation for the Python client for EveryAction. The user documentation is available
[here](https://python-client-for-everyaction.readthedocs.io/en/latest/).

## Create Virtual Environment

```
make venv
```

## Activate Virtual Environment

```
source venv/bin/activate
```

This step is unnecessary for running any Makefile targets, but is useful for ad-hoc testing/experimentation or to pass
custom options to `pytest`.

## Run Tests

```
make test
```

To run only the last failed tests:

```
make test-failed
```

To pass custom options to `pytest`, activate the virtual environment and invoke `pytest` on *everyaction/test* directly.

## Make Documentation

```
make docs
```

Resulting documentation will be found in the "docs" folder. Note that the actual documentation is hosted on ReadTheDocs
and thus generated documentation should not be committed.

## Check Documentation Links

This command will report on what links in the generated documentation are valid: 

```
make linkcheck
```

Note that it will report links that depend on the built Sphinx HTML as broken, so just ignore those. Useful for testing
that EveryAction documentation links are up-to-date.

## Remove Generated Files

```
make clean
```

## Publish Changes

This command increments the project version and pushes changes to GitHub:

```
make publish
```

You need to have already committed your changes and have no untracked files, otherwise this will fail.
