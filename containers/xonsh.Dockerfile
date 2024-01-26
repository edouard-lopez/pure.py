# Speficy fish version to use during build 
# docker build -t <image> --build-arg VERSION=<version>
ARG VERSION=latest
FROM python:3.5-alpine3.7

# Redeclare ARG so its value is available after FROM (cf. https://github.com/moby/moby/issues/34129#issuecomment-417609075)
ARG VERSION
RUN printf "\nBuilding \e[38;5;27mXonsh-%s\e[m\n\n" ${VERSION}

# Requirements
USER root
RUN apk add --no-cache \
    git \
    py3-pip
RUN python3 -m pip install --upgrade \
    pip \
    pipenv \
    xonsh

# Install
RUN adduser -s /bin/xonsh -D pure
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
		--no-cache-dir \ 
		/home/pure/.pure/

# Configure
USER pure
COPY --chown=pure:pure ./install/configure.xonsh /home/pure/.pure/install/
COPY --chown=pure:pure ./config/prompt.xonsh /home/pure/.pure/config/prompt.xonsh
RUN xonsh $HOME/.pure/install/configure.xonsh

CMD ["xonsh"]