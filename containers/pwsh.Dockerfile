# Speficy fish version to use during build 
# docker build -t <image> --build-arg VERSION=<version>
ARG VERSION=latest
FROM mcr.microsoft.com/powershell:${VERSION}

# Redeclare ARG so its value is available after FROM (cf. https://github.com/moby/moby/issues/34129#issuecomment-417609075)
ARG VERSION
RUN printf "\nBuilding \e[38;5;27mPowershell-%s\e[m\n\n" ${VERSION}

USER root
RUN apk add --no-cache python3
RUN adduser --shell /usr/bin/pwsh -D pure

USER pure
WORKDIR /home/pure/.pure/
COPY --chown=pure:pure . /home/pure/.pure/

CMD [ "pwsh" ]