#!/usr/bin/env bash

set -e

version=3.27.3

# determine OS and arch
if [[ "$OSTYPE" == "linux-gnu" ]]; then
os="linux"
arch=$(uname -m)
stub=""
[[ "$arch" == "arm64" ]] && arch="aarch64"
elif [[ "$OSTYPE" == "darwin"* ]]; then
os="macos"
arch="universal"
stub="CMake.app/Contents/"
else
echo "$OSTYPE not supported"
exit 1
fi

# compose URL
name=cmake-${version}-${os}-${arch}
archive=${name}.tar.gz
archive_path=$HOME/${archive}
url=https://github.com/Kitware/CMake/releases/download/v${version}/${archive}

# download and extract CMake

echo "${url} => ${archive_path}"
curl --location --no-clobber --output ${archive_path} ${url}

tar -x -v -f ${archive_path} -C $HOME

# prompt user to default shell to this new CMake
export PATH=$HOME/$name/bin:$PATH

case "$SHELL" in
*/zsh)
shell="zsh";;
*/bash)
shell="bash";;
*)
echo "unknown shell $SHELL"
esac

[[ -z ${shell+x} ]] || echo "please add the following line to file $HOME/.${shell}rc"
echo "export PATH=$HOME/$name/${stub}bin:\$PATH"
