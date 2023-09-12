# Thonny IDE

[Thonny](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/2)
provides a graphical IDE for Python, including MicroPython on microcontrollers like the Pi Pico.
Note: for Thonny to work, you must have
[MicroPython](./micropython.md)
installed on your Pico.

## Install Thonny

If you already have Python on your computer, you can type in Terminal:

```sh
python -m pip install thonny
```

and then to start Thonny type in Terminal:

```sh
thonny
```

### macOS

If on macOS and you used the Thonny .pkg file from
[Thonny.org](https://thonny.org/),
use macOS Spotlight to find Thonny and start it--press Command-space and type "thonny" and press Enter.

### Windows

If on Windows and you used the Thonny .exe file from
[Thonny.org](https://thonny.org/),
Thonny is installed in the Windows Start menu under Thonny.

## Initial connection

Start Thonny and click "Tools - Interpreter" and select "MicroPython (Raspberry Pi Pico)".
The "port or WebREPL" should select "Try to detect port automatically" unless you want to
[manually specify a port](./console.md).

Upon clicking "OK" and with a Pico already connected, Thonny shell should show a message like

> MicroPython v1.20.0 on 2023-04-26; Raspberry Pi Pico with RP2040

If you don't see that message or get a connection error, try:

* clicking the Red "stop" button in the Thonny toolbar
* unplugging and plugging in the Pico and click the red "stop" button in the Thonny toolbar

This should get you to the MicroPython prompt ">>>" upon pressing Enter.

Save Python code to the Pico by pressing Ctrl-s or Command-s and choose to save to the Pico.
You can name the file whatever you like and run it from Thonny.
If you name the file "main.py", that program will always run automatically when the Pico powers up.

## Run program

If you named the Pico Python file "main.py" it will run automatically.
Pressing the "stop" button in Thonny will stop the program and restart main.py.

## Troubleshooting

If when running the MicroPython code you get an error like:

> ModuleNotFoundError: No module named 'machine'

this usually means you're running the code on your computer instead of the Pico.
In Thonny, click "Tools - Interpreter" and select "MicroPython (Raspberry Pi Pico)" to automatically run on the Pico instead of your laptop.
