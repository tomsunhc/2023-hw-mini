# Fall 2023 Hardware miniproject Raspberry Pi Pico

[![ci](https://github.com/BostonUniversitySeniorDesign/2023-hw-mini/actions/workflows/ci.yml/badge.svg)](https://github.com/BostonUniversitySeniorDesign/2023-hw-mini/actions/workflows/ci.yml)

---

[Miniproject assignment](./assignment.md)

---

This project is accomplished using the Raspberry Pi Pico, Photocell, breadboard and associated wires and resistors.
The student laptop is used to program the Pico--Pico software development kit (SDK) work on macOS, Windows, and Linux.

Install
[CMake, Git, and the 32-bit ARM compiler](./doc/compiler.md)
on the laptop.
Then this software project can be built, which downloads the
[Pico SDK](./doc/pico-sdk.md)
automatically.

Configure the CMake project once, unless changing an option or doing a major change to code:

```sh
cmake -B build
```

To save build time, pick a particular target to build like:

```sh
cmake --build build -t pwm_led_fade
```

This builds file "build/src/pwm/led_fade/pwm_led_fade.uf2".
The .uf2 file is the binary image to
[upload to the Pico board](./doc/upload.md)
for a particular program.

---

[Troubleshooting](./doc/trouble.md)
