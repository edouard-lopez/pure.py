# Override ZSH_IMAGE to test a different Python Alpine image. The default digest is immutable.
ARG ZSH_IMAGE=python:3.12-alpine3.19@sha256:017a82f185bf6f10e62156f3e89b7e694d56d613b5a3f4dbf1d28f1014a972ed
FROM ${ZSH_IMAGE}

ARG ZSH_IMAGE
RUN printf "\nBuilding from \e[38;5;27m%s\e[m\n\n" "${ZSH_IMAGE}"

# Requirements
USER root
RUN apk add --no-cache \
    zsh \
    git \
    py3-pip
ENV PIP_BREAK_SYSTEM_PACKAGES=1
ARG BOOTSTRAP_PIPENV_VERSION=2024.4.1
RUN python3 -m pip install --no-cache-dir "pipenv==${BOOTSTRAP_PIPENV_VERSION}"

# Install
RUN adduser -s /usr/bin/zsh -D pure
WORKDIR /home/pure/.pure/
COPY --chown=pure:pure \
    ./Pipfile \
    ./Pipfile.lock \
    /home/pure/.pure/
RUN pipenv install \
    --deploy \
    --system \
    --ignore-pipfile
COPY --chown=pure:pure \
    ./README.md \
    ./setup.py \
    /home/pure/.pure/
COPY --chown=pure:pure ./pure/ /home/pure/.pure/pure/
RUN python3 -m pip install --no-cache-dir --editable /home/pure/.pure/

# Configure
USER pure
COPY --chown=pure:pure ./install/configure.zsh /home/pure/.pure/install/
COPY --chown=pure:pure ./config/prompt.zsh /home/pure/.pure/config/prompt.zsh
RUN echo '#' > /home/pure/.zshrc
RUN zsh -x "$HOME/.pure/install/configure.zsh"

CMD ["/bin/zsh","-l"]