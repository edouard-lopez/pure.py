# Speficy fish version to use during build 
# docker build -t <image> --build-arg VERSION=<version>
ARG VERSION=5.9-r2
FROM python:3.12-alpine3.19

# Redeclare ARG so its value is available after FROM (cf. https://github.com/moby/moby/issues/34129#issuecomment-417609075)
ARG VERSION
RUN printf "\nBuilding \e[38;5;27mZsh-%s\e[m\n\n" ${VERSION}

# Requirements
USER root
RUN apk add --no-cache \
    zsh \
    git \
    py3-pip
RUN python3 \
    -m pip install \
    --upgrade \
    pip \
    pipenv

# Install
RUN adduser -s /usr/bin/zsh -D pure
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
    --editable \ 
    /home/pure/.pure/

# Configure
USER pure
COPY --chown=pure:pure ./install/configure.zsh /home/pure/.pure/install/
COPY --chown=pure:pure ./config/prompt.zsh /home/pure/.pure/config/prompt.zsh
RUN echo '#' > /home/pure/.zshrc 
RUN zsh -x "$HOME/.pure/install/configure.zsh"


CMD ["/bin/zsh","-l"]