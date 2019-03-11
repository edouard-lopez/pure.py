# Speficy fish version to use during build 
# docker build -t <image> --build-arg VERSION=<version>
ARG VERSION=latest
FROM  mcandre/docker-ksh93:latest

# Redeclare ARG so its value is available after FROM (cf. https://github.com/moby/moby/issues/34129#issuecomment-417609075)
ARG VERSION
RUN printf "\nBuilding \e[38;5;27mKsh-%s\e[m\n\n" ${VERSION}

RUN yes '' | adduser --shell /bin/ksh --disabled-password pure

USER pure
WORKDIR /home/pure/.pure/
COPY --chown=pure:pure . /home/pure/.pure/

CMD ["/bin/ksh"]