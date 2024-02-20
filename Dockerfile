FROM ruby:3.2.3-alpine

ARG USER_ID=1000
ARG GROUP_ID=1000
ARG USER=jekyll
ARG GROUP=jekyll

ENV GEM_HOME=/home/${USER}/gems
ENV PATH="${GEM_HOME}:${PATH}"

EXPOSE 4000

WORKDIR /opt/code

# Create user and group to chown the files, so they are not owned by root
# See https://github.com/moby/moby/issues/35018
#
# This also requires changing the owner of the folder created by WORKDIR
# See https://github.com/moby/moby/issues/36408
RUN addgroup --gid ${GROUP_ID} jekyll && \
    adduser --disabled-password --gecos "" --uid ${USER_ID} --ingroup ${GROUP} ${USER} && \
    chown -R ${USER}:${GROUP} /home/${USER} /opt/code

RUN apk update && \
    apk add --no-cache \
        g++ \
        gcc \
        libc-dev \
        make \
        nodejs \
        openssl-dev \
        ruby-full

# Change to non-root user before installing Gems
USER ${USER}:${GROUP}

# Copy entire source code with appropriate owner
COPY --chown=${USER}:${GROUP} . .

# Finally, install Jekyll, Bundler, and other dependencies
RUN bundle install

CMD bundle exec jekyll serve --host 0.0.0.0
