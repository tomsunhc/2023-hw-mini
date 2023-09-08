# C / C++ on the Pico via Pico SDK

Install
[CMake, Git, and the 32-bit ARM compiler](./compiler.md)
on the laptop.
Then this software project can be built, which downloads the
[Pico SDK](https://www.raspberrypi.com/documentation/pico-sdk/)
automatically.

Configure the CMake project once from the top-level "2023-hw-mini/" directory.
Note that you must use "git clone" to get the project, so that you have all the cross-compiler scripts CMake needs.

```sh
git clone https://github.com/BostonUniversitySeniorDesign/2023-hw-mini

cd 2023-hw-mini
```

This CMake configure command is only needed once, unless subsequently changing a CMake project option:

```sh
cmake -B build
```

Build the .uf2 file(s) to upload to the Pico.
This command is run each time a code change is made you wish to compile:

```sh
cmake --build build
```

This builds file "build/src/pwm/led_fade/pwm_led_fade.uf2".
The .uf2 file is the binary image to
[upload to the Pico board](./upload.md)
for a particular program.

## Troubleshooting CMake

In general, CMake must be run from or specify the top-level project source directory containing CMakeLists.txt, NOT from the subdirectories that also have CMakeLists.txt.
A symptom of this problem is errors like

>   No project() command is present.  The top-level CMakeLists.txt file must
>  contain a literal, direct call to the project() command.

You can specific the CMake top-level source directory and build directory like:

```sh
cmake -S 2023-hw-mini/ -B /tmp/build

cmake --build /tmp/build
```

## Manual Pico SDK install

**NOTE: This usually isn't necessary--just use the automatic process above.**

Download the Pico SDK like:

```sh
cd

git clone https://github.com/raspberrypi/pico-sdk.git

git switch -C pico-sdk -d 1.5.1
```

The "git switch" command puts the SDK to a specific
[release version](https://github.com/raspberrypi/pico-sdk/releases),
which is general is a good Git practice to use a known state of another software project.

For convenience, set environment variable PICO_SDK_PATH so you don't have to type it each time you configure CMake.

* macOS: add to file ~/.zprofile

    ```sh
    export PICO_SDK_PATH=$HOME/pico-sdk
    ```
* Linux / Windows Subsystem for Linux: add to file ~/.bashrc

    ```sh
    export PICO_SDK_PATH=$HOME/pico-sdk
    ```
