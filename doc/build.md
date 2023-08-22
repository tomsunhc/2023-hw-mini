# CMake build

CMake is the most popular build system and supports a wide array of computing platforms.
CMake has two main steps of use: configure and build.

## CMake Configure

CMake configure step allows user options to be set and good CMake scripts test for required conditions to be met to help avoid confusing build errors.

```sh
cmake -B build
```

is a minimal CMake configure statement executed from the top-level directory containing the CMakeLists.txt file, and building under that in directory "build/".

## CMake Build

The build step executes the underlying build system, typically GNU Make or Ninja.

```sh
cmake --build build
```

where "build" is the relative or absolute path to the build directory specified in the "cmake -B" configure step.

## Example CMake output

```sh
cmake -B build
```

gives results on Linux like:

```
PICO_SDK_PATH is /home/runner/work/2023-hw-mini/2023-hw-mini/build/_deps/pico_sdk-src
PICO platform is rp2040.
Defaulting PICO platform compiler to pico_arm_gcc since not specified.
PICO compiler is pico_arm_gcc
-- The C compiler identification is GNU 10.3.1
-- The CXX compiler identification is GNU 10.3.1
-- The ASM compiler identification is GNU
-- Found assembler: /usr/bin/arm-none-eabi-gcc
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/arm-none-eabi-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/arm-none-eabi-g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- CMAKE_EXE_LINKER_FLAGS_INIT:
CMAKE_C_FLAGS: -mcpu=cortex-m0plus -mthumb
CMAKE_CXX_FLAGS: -mcpu=cortex-m0plus -mthumb
Build type is Release
PICO target board is pico.
Using board configuration from /home/runner/work/2023-hw-mini/2023-hw-mini/build/_deps/pico_sdk-src/src/boards/include/boards/pico.h
-- Found Python3: /usr/bin/python3.10 (found version "3.10.12") found components: Interpreter
TinyUSB available at /home/runner/work/2023-hw-mini/2023-hw-mini/build/_deps/pico_sdk-src/lib/tinyusb/src/portable/raspberrypi/rp2040; enabling build support for USB.
-- Configuring done (7.7s)
-- Generating done (0.1s)
-- Build files have been written to: /home/runner/work/2023-hw-mini/2023-hw-mini/build
```

on macOS the configure output is like:

```


```

---

If a CMake configure error occurs,
[troubleshooting](./trouble.md)
is required to see what's missing/incorrect on the developer laptop.
