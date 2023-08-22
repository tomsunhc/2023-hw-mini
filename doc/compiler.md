# Cross compiler install

Microcontrollers generally use a different CPU architecture than the developer's laptop.
This implies a
[cross compiler](https://en.wikipedia.org/wiki/Cross_compiler)
is needed to build code for the microcontroller on the laptop.
It's straightforward to install the 32-bit ARM C/C++ cross-compiler on macOS, Windows, and Linux.

Please follow the section relevant to the laptop operating system.
About 2..5 gigabytes of hard drive space is required by the Pico SDK and associated tools.

Git, CMake and a cross compiler are used by almost all full projects as well.

You can use this
[compiler install script on Linux and macOS](../scripts/install_crosss_compiler.sh)
or manually below.

## macOS

[Homebrew](https://brew.sh)
is popular on macOS to get a wide variety of development and creative software packages.

Install Git, CMake build system, and ARM cross-compiler by:

```sh
brew install cmake git

brew install --cask gcc-arm-embedded
```

The cross-compiler executables have a prefix "arm-none-eabi-" that are linked into `$(brew --prefix)/bin` for easy use from the command line.

It's likely the macOS laptop has an Apple Silicon CPU.
If so, it's necessary to
[enable Rosetta](https://support.apple.com/en-us/HT211861).
Rosetta enables most x86 apps on Apple Silicon at nearly full performance.

## Linux

Install Git, CMake build system, and ARM cross-compiler on:

* laptop/desktop with Ubuntu / Debian-like distros
* full Raspberry Pi (e.g. Raspberry Pi 4)

```sh
sudo apt update

sudo apt install git make cmake g++ gcc-arm-none-eabi libnewlib-arm-none-eabi libstdc++-arm-none-eabi-newlib
```

NOTE: if upon `cmake -B build` you get an immediate error about CMake being too old,
please install a newer CMake via
[scripts/install_cmake.sh](../scripts/install_cmake.sh)

## Windows

Windows Subsystem for Linux (WSL) is useful for many projects including the Raspberry Pi Pico SDK.
WSL can be the easiest way to work with non-Windows projects on Windows.

The Ubuntu WSL process takes about 10 minutes depending on download speed.
WSL can be installed via the
[Microsoft Store Ubuntu app](https://apps.microsoft.com/store/detail/ubuntu/9PDXGNCFSCZV).
If the Microsoft Store isn't available on the computer, it is also possible to install [Ubuntu WSL manually](https://docs.microsoft.com/en-us/windows/wsl/install).

[WSL can access](https://docs.microsoft.com/en-us/windows/wsl/filesystems)
the native Windows filesystem.
WSL sees the native Windows filesystem "C:" in WSL via "/mnt/c".
Use the native Windows drive under "/mnt/c/pico" from WSL.
Then you can use Windows File Explorer in path "C:/pico" to
[drag and drop .uf2 file to Pico](./upload.md).

The cross-compiler install on WSL Ubuntu is just like plain Linux in the section above.

To make switching between Windows and WSL easier, we optionally use
[Windows Terminal](https://docs.microsoft.com/en-us/windows/terminal/install).

### Alternative: Visual Studio

The Visual Studio cross-compiler setup is described in Section 9.2 of the
[Pico install guide](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf).
I used WSL as above instead.
