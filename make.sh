#!/bin/bash

here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

packages="python3-dev python3-venv"
envname='.env'

if test ! -d $envname; then

  sudo apt-get install $packages
  python3 -m venv $here/$envname

fi

bash $here/src/samplelib/make.sh

$here/.venv/bin/python $here/src/__init__.py
