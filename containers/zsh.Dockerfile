# Speficy fish version to use during build 
# docker build -t <image> --build-arg VERSION=<version>
ARG VERSION=master
FROM zshusers/zsh-${VERSION}:latest

# Redeclare ARG so its value is available after FROM (cf. https://github.com/moby/moby/issues/34129#issuecomment-417609075)
ARG VERSION
RUN printf "\nBuilding \e[38;5;27mZsh-%s\e[m\n\n" ${VERSION}

RUN yes '' | adduser --shell /usr/bin/zsh --disabled-password pure
RUN echo '#' > /home/pure/.zshrc 
RUN chown pure:pure /home/pure/.zshrc 

USER pure
WORKDIR /home/pure/.pure/
COPY --chown=pure:pure . /home/pure/.pure/

CMD ["/usr/bin/zsh","-l"]