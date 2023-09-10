# Thonny IDE

[Thonny](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/2)
provides a graphical IDE for Python, including MicroPython on microcontrollers like the Pi Pico.
After installing Thonny, click "Tools - Interpreter" and select "MicroPython (Raspberry Pi Pico)".
The "port or WebREPL" should select "Try to detect port automatically" unless you want to
[manually specify a port](./console.md).
Upon clicking "OK" and with a Pico already connected, Thonny shell should show a message like

> MicroPython v1.20.0 on 2023-04-26; Raspberry Pi Pico with RP2040

Save Python code to the Pico by pressing Ctrl-s or Command-s and choose to save to the Pico.
Choose an arbitrary filename like "flash.py" and click OK.
Then press F5 to run the program.
