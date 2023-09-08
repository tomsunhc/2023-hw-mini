# Fall 2023 Hardware miniproject Raspberry Pi Pico

[![ci](https://github.com/BostonUniversitySeniorDesign/2023-hw-mini/actions/workflows/ci.yml/badge.svg)](https://github.com/BostonUniversitySeniorDesign/2023-hw-mini/actions/workflows/ci.yml)

[ASSIGNMENT](./assigment.md)

This project uses the Raspberry
[Pi Pico H](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
(no wireless, with header pins).
A breadboard, Pi Pico H, photocell, resistor, and wire kit are provided to each hardware miniproject student for the [circuit](./doc/circuit.md).
Each student must provide a USB cable that connects to their macOS, Windows, or Linux laptop and has a micro-USB connector on the other end to plug into the Pico.
The student laptop is used to program the Pico.
The laptop software works on macOS, Windows, and Linux.

Use a programming language of your choice such as:

* [MicroPython](./doc/micropython.md) (recommended)
* C/C++ via [Pico SDK](./doc/pico-sdk.md) (optional)

We will be reading an analog voltage using the onboard Pico ADC and indicating the measurement using the onboard Pico LED in a **multithread program** using both CPU cores of the Pico RP2040 dual-core CPU.

---

[Troubleshooting](./doc/trouble.md)

Reference: [Getting Started with Pi Pico book](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf)
