#!/bin/sh

source .venv/bin/activate
make install-test
make test