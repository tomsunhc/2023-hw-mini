#!/usr/bin/env bash

set -e

# determine OS and arch
case "$OSTYPE" in
linux*)
sudo apt update
sudo apt install git cmake g++ gcc-arm-none-eabi libnewlib-arm-none-eabi libstdc++-arm-none-eabi-newlib;;
darwin*)
brew install git cmake
brew install --cask gcc-arm-embedded;;
*)
echo "$OSTYPE not supported"
exit 1
esac
