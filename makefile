 #!/usr/bin/make -sf

# force use of Bash
SHELL := /bin/bash
INTERACTIVE=true

BASH_VERSION := 4.4
ELVISH_VERSION := latest  # pre-release
FISH_VERSION := 3.5.1
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
	pytest --verbose --cov=pure tests/

.PHONY: tests-unit-only
tests-unit-only:
	pytest --verbose --cov=pure tests/ --ignore=tests/integration_test.py


shell = $*
shell_name = $(shell echo '$*' | tr '[:lower:]' '[:upper:]')
shell_version = ${${shell_name}_VERSION}

show-versions:
	@echo "Bash: ${BASH_VERSION}"
	@echo "Elvish: ${ELVISH_VERSION}"
	@echo "Fish: ${FISH_VERSION}"
	@echo "Ksh: ${KSH_VERSION}"
	@echo "Pwsh: ${PWSH_VERSION}"
	@echo "Tcsh: ${TCSH_VERSION}"
	@echo "Xonsh: ${XONSH_VERSION}"
	@echo "Zsh: ${ZSH_VERSION}"

.PHONY: build-pure-on-%
build-pure-on-%:
	@echo ${shell} ${shell_version}
	docker build \
		--file ./containers/${shell}.Dockerfile \
		--tag=pure-on-${shell}-${shell_version} \
		--build-arg ARGS="VERSION=${shell_version}" \
		--pull \
		./

.PHONY: dev-pure-on-%
dev-pure-on-%:
	@echo ${shell} ${shell_version}
	docker run \
		--name run-pure-on-${shell} \
		--rm \
		--interactive \
		--tty \
		--volume=$$PWD:/home/pure/.pure/ \
		pure-on-${shell}-${shell_version}


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