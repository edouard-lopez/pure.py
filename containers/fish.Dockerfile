# syntax=docker/dockerfile:1.4
# Override FISH_IMAGE to test a different Fish image. The default digest is immutable.
ARG FISH_IMAGE=purefish/docker-fish@sha256:62169d3002b4a9425b2672cbfb7fb5ecf988b051bc47af506b6b5cc6c47d5112
FROM ${FISH_IMAGE}

ARG FISH_IMAGE
RUN printf "\nBuilding from \e[38;5;27m%s\e[m\n\n" "${FISH_IMAGE}"

USER root
RUN apk add \
    --no-cache \
    coreutils \
    python3 \
    py3-pip
ENV PIP_BREAK_SYSTEM_PACKAGES=1
ARG BOOTSTRAP_PIPENV_VERSION=2024.4.1
RUN python3 -m pip install --no-cache-dir "pipenv==${BOOTSTRAP_PIPENV_VERSION}"

# Install
RUN adduser --shell /usr/bin/fish -D pure
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
COPY --chown=pure:pure ./install/configure.fish /home/pure/.pure/install/
COPY --chown=pure:pure ./config/fish_prompt.fish /home/pure/.pure/config/fish_prompt.fish
RUN fish $HOME/.pure/install/configure.fish

CMD ["fish"]