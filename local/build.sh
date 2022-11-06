#!/bin/bash
docker build . -t python-poetry-build

docker run --rm --workdir /github/workspace --user root -v "${PWD}":/github/workspace --entrypoint /bin/bash python-poetry-build -c "\
    pip install poetry --cache-dir=.pip; \
    poetry export -f requirements.txt  -o requirements.txt --without-hashes; \
    pip install -t dist/src -r requirements.txt --cache-dir=.pip ; \
    cp -rv --exclude=dist ./* dist/src/; \
    rm requirements.txt;"