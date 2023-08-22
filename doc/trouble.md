# Troubleshooting

CMake uses environment variables to populate options including compile and link flags.
The configure step prints a few key variables.

Example: if missing [cross compiler](./compiler.md), CMake errors like:

> Compiler 'arm-none-eabi-gcc' not found, you can specify search path with "PICO_TOOLCHAIN_PATH".
