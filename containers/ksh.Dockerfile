# Speficy fish version to use during build 
# docker build -t <image> --build-arg VERSION=<version>
ARG VERSION=latest
FROM  mcandre/docker-ksh93:${VERSION}

# Redeclare ARG so its value is available after FROM (cf. https://github.com/moby/moby/issues/34129#issuecomment-417609075)
ARG VERSION
RUN printf "\nBuilding \e[38;5;27mKsh-%s\e[m\n\n" ${VERSION}

USER root
WORKDIR /home/root/.pure/
COPY --chown=root:root . /home/root/.pure/

CMD ["/bin/ksh"]