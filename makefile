#!/usr/bin/make -sf

# force use of Bash
SHELL := /bin/bash
INTERACTIVE=true

.PHONY: install-requirements
install-requirements:
	python3 -m pip install \
		--user \
		--upgrade \
			setuptools \
			wheel \
			twine

.PHONY: generate-package
generate-package:
	python3 setup.py sdist bdist_wheel

.PHONY: upload-package
upload-package:
	@printf '\e[0;35m%-6s\e[m\n' "Pypi username:"
	@python3 -m twine upload \
		--repository-url https://test.pypi.org/legacy/ \
		dist/*

.PHONY: setup-keyring
setup-keyring:
	python3 -m keyring set https://test.pypi.org/legacy/ edouard-lopez
	# python3 -m keyring set https://upload.pypi.org/legacy/ edouard-lopez