# MicroPython

[MicroPython](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
is a popular method to use Python script on embedded systems including the Pi Pico.
The
[Pico MicroPython SDK](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf)
is tailored specifically to the Pi Pico hardware ecosystem.
In general across computing platforms, compiled code such as C / C++ can offer better computing performance, but scripted languages such as Python are often easier to develop in.
This application is not computationally demanding.
In general, we often prototype in a scripted language like Python, only moving to compiled languages if necessary to compute fast enough.

MicroPython
[standard library](https://docs.micropython.org/en/latest/library/index.html#micropython-libraries)
supports typical Python features including
[asyncio concurrency](https://docs.micropython.org/en/latest/library/asyncio.html)
and libraries specific to the
[Pico](https://docs.micropython.org/en/latest/library/index.html#libraries-specific-to-the-rp2040).
The RP2040 dual core CPU of the Pico supports MicroPython GIL-less VM, so
[parallel executing threads](https://github.com/raspberrypi/pico-micropython-examples/blob/master/multicore/multicore.py)
are possible in Python on the Pico.

Practically speaking, certain tasks I see students using the much more expensive and far more power-hungry full Raspberry Pi ARM for can often be done on the Pi Pico.
Power and size are often key limitations in class projects that might be solved if the problem can fit into a Pi Pico vs. a full ARM Raspberry Pi.

After installing MicroPython below, the Pico will not visibly do anything.
To interact with the Pico Python REPL, edit and upload Python scripts that autorun on the Pico, choices include:

* [Thonny IDE](./thonny.md) (graphical interface, easier to use)
* [rshell](./rshell.md)

## Install MicroPython

[Install MicroPython](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#drag-and-drop-micropython)
from the laptop using the correct UF2 file for the Pi Pico hardware--that is the plain Pico without wireless.
Assuming you've downloaded the file named like "rp2-pico-20230426-v1.20.0.uf2" copy this to the Pi Pico by first holding down the BOOTSEL button, plugging into laptop USB, then release the BOOTSEL button.

![bootsel switch](./bootsel.png)

You don't have to use the BOOTSEL button any more after installing MicroPython, as MicroPython will always start when the Pico is powered up.

### Windows

Windows File Explorer will show the Pico under "This PC" "RPI-RP2".
If you don't see it, check in Windows Device Manager: "Disk drives", "RPI RP2 USB Device".

Copy the "rp2-pico-20230426-v1.20.0.uf2" file to the RPI-RP2 device in File Explorer.

### macOS

The Pico appears on the Desktop as "RPI-RP2" with a grey box icon.
The Pico is also seen in Finder in the left hand column under "Locations" as "RPI-RP2".
The mount point accessible via Terminal is "/Volumes/RPI-RP2".
Copy the .uf2 file to the Pico:

```sh
cp ~/Downloads/rp2-pico-20230426-v1.20.0.uf2 /Volumes/RPI-RP2/
```

The Pico will immediately reboot and disconnect from the laptop, and show a flashing LED.

### Linux

On Linux, the Pico will typically in the distro file explorer as "RPI_RP2", whether using a full Raspberry Pi or Linux laptop.
The exact device path varies between Linux distros if looking to use Terminal.
Find the mount point and then copy the file as in Windows or macOS.

```sh
lsblk
```
