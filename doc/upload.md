# Pico Drag-n-Drop upload

A convenient way to upload .uf2 compiled binaries to the Pico is the Drag-n-drop mode.
Although nowadays we've become accustomed to not thinking about filesystems, when working with computer programming and embedded systems in general, we need to have a basic familiarity of filesystem use.

This requires a **micro-USB cable** that connects between the laptop and Pico.
Check which type of USB port the laptop has.
Almost all laptops have a USB-C or USB-A port.
Some USB cables don't have the data pins connected.
Suitable USB cables can be obtained from many local stores.

Connect the micro-USB to the Pico.
Before and as you plug the other end of the cable into your laptop, hold down the "BOOTSEL" button on the Pico.
The Pico will appear almost instantly (while holding down BOOTSEL) as an external flash drive in the file browser of the laptop.
Then release BOOTSEL button.

![bootsel switch](./bootsel.png)

Once the file is copied, the **Pico instantly reboots**, disconnecting from the laptop, and runs the program.

To upload a new version of the program, repeat the process above.
That is, unplug from USB, hold down BOOTSEL button, plug in USB, and release BOOTSEL.

Be careful not to break the micro-USB port on the Pico.

## Windows

Windows File Explorer will show the Pico under "This PC" "RPI-RP2".
If you don't see it, check in Windows Device Manager: "Disk drives", "RPI RP2 USB Device".

[WSL can use](https://docs.microsoft.com/en-us/windows/wsl/filesystems)
the native Windows filesystem and vice versa.
From Windows Command Prompt, see the WSL filesystem by:

```pwsh
explorer \\wsl$
```

## macOS

The Pico appears on the Desktop as "RPI-RP2" with a grey box icon.
The Pico is also seen in Finder in the left hand column under "Locations" as "RPI-RP2".
The mount point accessible via Terminal is "/Volumes/RPI-RP2".

From the "2023-hw-mini/" directory, copy the .uf2 file to the Pico:

```sh
cp build/src/pwm/led_fade/pwm_led_fade.uf2 /Volumes/RPI-RP2/
```

The Pico will immediately reboot and disconnect from the laptop, and show a flashing LED.

## Linux

On Linux, the Pico will typically in the distro file explorer as "RPI_RP2", whether using a full Raspberry Pi or Linux laptop.
The exact device path varies between Linux distros if looking to use Terminal.
Find the mount point:

```sh
lsblk
```
