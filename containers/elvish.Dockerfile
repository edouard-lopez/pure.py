# Speficy fish version to use during build 
# docker build -t <image> --build-arg VERSION=<version>
ARG VERSION=latest
FROM theelves/elvish:${VERSION}

# Redeclare ARG so its value is available after FROM (cf. https://github.com/moby/moby/issues/34129#issuecomment-417609075)
ARG VERSION
RUN printf "\nBuilding \e[38;5;27mElvish-%s\e[m\n\n" ${VERSION}

USER root
RUN apk add \
    --no-cache \
    python3
RUN adduser --shell /bin/elvish -D pure

USER pure
WORKDIR /home/pure/.pure/
COPY --chown=pure:pure . /home/pure/.pure/
RUN elvish $HOME/.pure/install/configure.elv

CMD ["/bin/elvish"]