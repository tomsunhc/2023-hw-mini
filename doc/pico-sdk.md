# Download Pico SDK

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
