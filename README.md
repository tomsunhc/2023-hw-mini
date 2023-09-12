# Fall 2023 Hardware miniproject Raspberry Pi Pico

[![ci](https://github.com/BostonUniversitySeniorDesign/2023-hw-mini/actions/workflows/ci.yml/badge.svg)](https://github.com/BostonUniversitySeniorDesign/2023-hw-mini/actions/workflows/ci.yml)

[ASSIGNMENT](./assignment/)

This project uses the Raspberry
[Pi Pico H](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
(no wireless, with header pins).
A breadboard, Pi Pico H, photocell, resistor, and wire kit are provided to each hardware miniproject student for the [circuit](./doc/circuit.md).
Each student must provide a USB cable that connects to their macOS, Windows, or Linux laptop and has a micro-USB connector on the other end to plug into the Pico.
The student laptop is used to program the Pico.
The laptop software works on macOS, Windows, and Linux.

This miniproject focuses on using
[MicroPython](./doc/micropython.md)
using
[Thonny IDE](./doc/thonny.md).
You're welcome to other IDE and interface such as Visual Studio Code or
[rshell](./doc/rshell.md),
but generally folks find the Thonny IDE to be faster and easier to work with.

We will be reading an analog voltage using the onboard Pico ADC and indicating the measurement using the onboard Pico LED in a **multithread program** using both CPU cores of the Pico RP2040 dual-core CPU.

---

[Troubleshooting](./doc/trouble.md)

* [Getting Started with Pi Pico book](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf)
* [MicroPython Tutorial for Pi Pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico)
