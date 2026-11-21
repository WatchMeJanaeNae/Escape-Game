#!/bin/bash

# remove unwanted VSCode extension(s)
if command -v code >/dev/null 2>&1; then
  sudo code --uninstall-extension eamodio.gitlens || true
fi

# change default git config to ignore chmod changes and symbolic links
git config core.fileMode false

# change pull to always rebase to eliminate common git error
git config pull.rebase true

# upgrade pip and install required packages
pip install --upgrade pip
pip install pytest