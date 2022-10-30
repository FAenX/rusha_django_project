#!/bin/bash

docker run --rm --workdir /github/workspace --user root -v "${PWD}":/github/workspace --entrypoint /bin/bash python:slim-buster -c "\
    pip install poetry --cache-dir=.pip; \
    poetry export -f requirements.txt  -o requirements.txt --without-hashes; \
    pip install -t dist/src -r requirements.txt --cache-dir=.pip ; \
    cp -rv --exclude=dist ./* dist/src/; \
    rm requirements.txt;"