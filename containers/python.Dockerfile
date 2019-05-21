# # # # # # # # # # # # # # # # # # # # # #
# This container is for debugging only
# # # # # # # # # # # # # # # # # # # # # #

# Speficy fish version to use during build
# docker build -t <image> --build-arg VERSION=<version>
ARG VERSION=3.5.6
FROM python:${VERSION}

# Redeclare ARG so its value is available after FROM (cf. https://github.com/moby/moby/issues/34129#issuecomment-417609075)
ARG VERSION
RUN printf "\nBuilding \e[38;5;27mFish-%s\e[m\n\n" ${VERSION}

USER root
RUN apt-get update && apt-get install --yes python3
RUN python3 -m pip install --upgrade \
    pip \
    pipenv

# Install
RUN yes '' | adduser --shell /bin/bash --disabled-password pure
WORKDIR /home/pure/.pure/
COPY --chown=pure:pure \
        ./Pipfile \
        ./Pipfile.lock \
        ./README.md \
        ./setup.py \
    /home/pure/.pure/
COPY --chown=pure:pure ./pure/ /home/pure/.pure/pure/
RUN pipenv install \
        --dev \
        --deploy \
        --system \
        --ignore-pipfile
RUN pip install --editable /home/pure/.pure/
RUN pip install \
        pathlib2

# Configure
USER pure
COPY --chown=pure:pure ./install/configure.bash /home/pure/.pure/install/
# COPY --chown=pure:pure ./config/prompt.bash /home/pure/.pure/config/prompt.bash
# RUN bash $HOME/.pure/install/configure.bash
RUN rm tests/__pycache__/ -rf


CMD ["bash"]