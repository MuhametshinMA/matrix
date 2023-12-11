FROM quay.io/school21/alpine:3.13

RUN apk --no-cache --upgrade add \
    build-base \
    make \
    valgrind \
    check \
    gawk \
    bash \
    python3 \
    py3-pip \
    check-dev

# RUN py3-pip install numpy

COPY . /src
WORKDIR "/src"
ENTRYPOINT "/bin/bash"
# CMD top