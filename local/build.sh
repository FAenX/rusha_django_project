#!/bin/bash

docker run --rm --workdir /github/workspace -v "${PWD}":/github/workspace --entrypoint /bin/bash python3.8 -c "\
    pip install poetry --cache-dir=.pip; \
    poetry export -f requirements.txt  -o requirements.txt --without-hashes; \
    pip install -t dist/src -r requirements.txt --cache-dir=.pip ; \
    cp -r src/* dist/src/; \
    rm requirements.txt;"