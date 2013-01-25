#!/bin/bash

## Auto-building Sphinx Docs
## http://jacobian.org/writing/auto-building-sphinx/

rm -rf _build/*;
make html;

watchmedo shell-command \
    --patterns="*.rst;*.py;*.html;*.css;*.conf" \
    --ignore-pattern='_build/*' \
    --recursive \
    --wait \
    --command='make html;'
