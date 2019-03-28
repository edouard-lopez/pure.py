#!/usr/bin/make -sf

# force use of Bash
SHELL := /bin/bash
INTERACTIVE=true

BASH_VERSION := 4.4
ELVISH_VERSION := latest  # pre-release
FISH_VERSION := 3.0.0
KSH_VERSION := 2012-08-01
PWSH_VERSION := 6.1.3-alpine-3.8
TCSH_VERSION := 6.20.00
XONSH_VERSION := latest
ZSH_VERSION := 5.4.2-r1

		
.PHONY: default
default: tests

.PHONY: tests
tests:
	clear
	pytest --verbose tests/

build-pure-on-%:
	@$(MAKE) --silent build-pure-on shell=$* > /dev/null

.PHONY: build-pure-on
build-pure-on:
	@$(MAKE) --silent build-on shell=${shell} VERSION="$${shell^^}_VERSION" 

.PHONY: build-on
build-on:
	docker build \
		--file ./containers/${shell}.Dockerfile \
		--tag=pure-on-${shell}-${${VERSION}} \
		--build-arg ARGS="VERSION=${${VERSION}}" \
		./

dev-pure-on-%:
	@$(MAKE) --silent dev-pure-on shell=$*

.PHONY: dev-pure-on
dev-pure-on:
	@$(MAKE) --silent dev-on shell=${shell} VERSION="$${shell^^}_VERSION"

.PHONY: dev-on
dev-on:
	@echo ${shell} ${VERSION}=${${VERSION}}
	docker run \
		--name run-pure-on-${shell} \
		--rm \
		--interactive \
		--tty \
		--volume=$$PWD:/home/pure/.pure/ \
		pure-on-${shell}-${${VERSION}}


.PHONY: install-requirements
install-requirements:
	apt install --yes \
		python3-dbus \
		python3-keyring \
		python-secretstorage
	pipenv install \
		--dev \
			setuptools \
			wheel \
			twine \
			keyring

.PHONY: generate-package
generate-package:
	rm build/ dist/ pure.egg-info/ -rf 
	python3 setup.py sdist bdist_wheel

.PHONY: upload-package
upload-package:
	twine upload --username edouard-lopez dist/*

.PHONY: setup-keyring
setup-keyring:
	 keyring set https://upload.pypi.org/legacy/ edouard-lopez