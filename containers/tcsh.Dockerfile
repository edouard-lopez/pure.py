# Speficy fish version to use during build 
# docker build -t <image> --build-arg VERSION=<version>
ARG VERSION=latest

FROM library/debian:stretch

RUN apt-get update && apt-get install --yes tcsh

# Redeclare ARG so its value is available after FROM (cf. https://github.com/moby/moby/issues/34129#issuecomment-417609075)
ARG VERSION
RUN printf "\nBuilding \e[38;5;27mTcsh-%s\e[m\n\n" ${VERSION}

RUN yes '' | adduser --shell /bin/tcsh --disabled-password pure
USER pure
WORKDIR /home/pure/.pure/
COPY --chown=pure:pure . /home/pure/.pure/

CMD ["/bin/tcsh"]
