#!/usr/bin/env bash

# Set local variables:
NAME=tic-toc
ANACONDA_ENV=tic-toc

cd ..

source activate $ANACONDA_ENV
pip install -r requirements_development.txt

# Remove previous builds:
rm -rf ./build/*
rm -rf ./dist/*

# Read package version:
VERSION=`python -c "from tic_toc import __version__ as ver; print(ver);"`

# Define the deployment platform:
target=https://test.pypi.org/legacy/
if [[ $# -eq 1 ]]; then
    target=https://upload.pypi.org/legacy/
fi

# Build the package:
python ./setup.py sdist bdist_wheel

# Upload the package:
read -r -p "Upload $NAME@$VERSION to '$target'? [y/N] " response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])+$ ]]; then
    twine upload ./dist/* --repository-url $target
fi
