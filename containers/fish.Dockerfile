# syntax=docker/dockerfile:1.4
# Speficy fish version to use during build 
# docker build -t <image> --build-arg VERSION=<version>
FROM purefish/docker-fish:latest

# Redeclare ARG so its value is available after FROM (cf. https://github.com/moby/moby/issues/34129#issuecomment-417609075)
ARG VERSION
RUN printf "\nBuilding \e[38;5;27mFish-%s\e[m\n\n" ${VERSION}

USER root
RUN apk add \
        --no-cache \
            coreutils \
            python3 
RUN python3 -m ensurepip
RUN python3 -m pip install \
        --upgrade \
            pip \
            pipenv

# Install
RUN adduser --shell /usr/bin/fish -D pure
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
RUN pip install \
        --editable /home/pure/.pure/

# Configure
USER pure
COPY --chown=pure:pure ./install/configure.fish /home/pure/.pure/install/
COPY --chown=pure:pure ./config/fish_prompt.fish /home/pure/.pure/config/fish_prompt.fish
RUN fish $HOME/.pure/install/configure.fish

CMD ["fish"]