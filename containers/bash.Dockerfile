# Speficy fish version to use during build 
# docker build -t <image> --build-arg VERSION=<version>
ARG VERSION=latest
FROM bash:${VERSION}

# Redeclare ARG so its value is available after FROM (cf. https://github.com/moby/moby/issues/34129#issuecomment-417609075)
ARG VERSION
RUN printf "\nBuilding \e[38;5;27mBash-%s\e[m\n\n" ${VERSION}

# Requirements
USER root
RUN apk add --no-cache \
    python3 \
    py3-pip \
    git
ENV PIP_BREAK_SYSTEM_PACKAGES 1
RUN python3 \
    -m pip install \
    --upgrade \
    pipenv

# Install
RUN adduser --shell /bin/bash -D pure
WORKDIR /home/pure/.pure/
COPY --chown=pure:pure \
    ./Pipfile \
    ./Pipfile.lock \
    ./README.md \
    ./setup.py \
    /home/pure/.pure/
COPY --chown=pure:pure ./pure/ /home/pure/.pure/pure/
RUN pipenv install \ 
		--deploy \ 
		--system \ 
		--ignore-pipfile
# hadolint ignore=DL3042
RUN pip install \ 
    --editable \ 
    /home/pure/.pure/

# Configure
USER pure
COPY --chown=pure:pure ./install/configure.bash /home/pure/.pure/install/
COPY --chown=pure:pure ./config/prompt.bash /home/pure/.pure/config/prompt.bash
RUN bash "$HOME/.pure/install/configure.bash"

CMD ["bash"]