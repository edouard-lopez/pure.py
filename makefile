#!/usr/bin/make -sf

# force use of Bash
SHELL := /bin/bash
INTERACTIVE=true

.PHONY: tests
tests:
	clear
	pytest --verbose tests/

.PHONY: build-pure-on-bash
build-pure-on-bash:
	$(MAKE) build-pure-on SHELL=bash VERSION="${BASH_VERSION}" ARGS="VERSION=${BASH_VERSION}"

.PHONY: build-pure-on-elvish
build-pure-on-elvish:
	$(MAKE) build-pure-on SHELL=elvish VERSION="${ELVISH_VERSION}" ARGS="VERSION=${ELVISH_VERSION}"

.PHONY: build-pure-on-fish
build-pure-on-fish:
	$(MAKE) build-pure-on SHELL=fish VERSION="${FISH_VERSION}" ARGS="VERSION=${FISH_VERSION}"

.PHONY: build-pure-on-ksh
build-pure-on-ksh:
	$(MAKE) build-pure-on SHELL=ksh VERSION="${KSH_VERSION}" ARGS="VERSION=${KSH_VERSION}"

.PHONY: build-pure-on-powershell
build-pure-on-powershell:
	$(MAKE) build-pure-on SHELL=powershell VERSION="${POWERSHELL_VERSION}" ARGS="VERSION=${POWERSHELL_VERSION}"

.PHONY: build-pure-on-tcsh
build-pure-on-tcsh:
	$(MAKE) build-pure-on SHELL=tcsh VERSION="${TCSH_VERSION}" ARGS="VERSION=${TCSH_VERSION}"

.PHONY: build-pure-on-zsh
build-pure-on-zsh:
	$(MAKE) build-pure-on SHELL=zsh VERSION="${ZSH_VERSION}" ARGS="VERSION=${ZSH_VERSION}"

.PHONY: build-pure-on
build-pure-on:
	docker build \
		--file ./containers/${SHELL}.Dockerfile \
		--build-arg ${ARGS} \
		--tag=pure-on-${SHELL}-${VERSION} \
		./


.PHONY: dev-pure-on-bash
dev-pure-on-bash:
	$(MAKE) dev-pure-on SHELL=bash VERSION="${BASH_VERSION}" ARGS="VERSION=${BASH_VERSION}"

.PHONY: dev-pure-on-elvish
dev-pure-on-elvish:
	$(MAKE) dev-pure-on SHELL=elvish VERSION="${ELVISH_VERSION}" ARGS="VERSION=${ELVISH_VERSION}"

.PHONY: dev-pure-on-fish
dev-pure-on-fish:
	$(MAKE) dev-pure-on SHELL=fish VERSION="${FISH_VERSION}" ARGS="VERSION=${FISH_VERSION}"

.PHONY: dev-pure-on-ksh
dev-pure-on-ksh:
	$(MAKE) dev-pure-on SHELL=ksh VERSION="${KSH_VERSION}" ARGS="VERSION=${KSH_VERSION}"

.PHONY: dev-pure-on-powershell
dev-pure-on-powershell:
	$(MAKE) dev-pure-on SHELL=powershell VERSION="${POWERSHELL_VERSION}" ARGS="VERSION=${POWERSHELL_VERSION}"

.PHONY: dev-pure-on-tcsh
dev-pure-on-tcsh:
	$(MAKE) dev-pure-on SHELL=tcsh VERSION="${TCSH_VERSION}" ARGS="VERSION=${TCSH_VERSION}"

.PHONY: dev-pure-on-zsh
dev-pure-on-zsh:
	$(MAKE) dev-pure-on SHELL=zsh VERSION="${ZSH_VERSION}" ARGS="VERSION=${ZSH_VERSION}"

.PHONY: dev-pure-on
dev-pure-on:
	docker run \
		--name run-pure-on-${SHELL} \
		--rm \
		--interactive \
		--tty \
		--volume=$$PWD:/home/nemo/.pure/ \
		pure-on-${SHELL}-${VERSION}


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