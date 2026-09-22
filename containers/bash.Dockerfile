# Override BASH_IMAGE to test a different Bash image. The default digest is immutable.
ARG BASH_IMAGE=bash@sha256:61962062d969cb46dfc2bad061d36342406fa485f64f246aa7e95693ca07df1f
FROM ${BASH_IMAGE}

ARG BASH_IMAGE
RUN printf "\nBuilding from \e[38;5;27m%s\e[m\n\n" "${BASH_IMAGE}"

# Requirements
USER root
RUN apk add --no-cache \
    python3 \
    py3-pip \
    git
ENV PIP_BREAK_SYSTEM_PACKAGES=1
ARG BOOTSTRAP_PIPENV_VERSION=2024.4.1
RUN python3 -m pip install --no-cache-dir "pipenv==${BOOTSTRAP_PIPENV_VERSION}"

# Install
RUN adduser --shell /bin/bash -D pure
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
COPY --chown=pure:pure ./install/configure.bash /home/pure/.pure/install/
COPY --chown=pure:pure ./config/prompt.bash /home/pure/.pure/config/prompt.bash
RUN bash "$HOME/.pure/install/configure.bash"

CMD ["bash"]