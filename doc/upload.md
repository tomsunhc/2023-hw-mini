# Pico Drag-n-Drop upload

A convenient way to upload .uf2 compiled binaries to the Pico is the Drag-n-drop mode.

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

Once the file is copied, the **Pico automatically reboots and runs the program**.

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

## Linux

On Linux, the Pico will typically in the distro file explorer as "RPI_RP2", whether using a full Raspberry Pi or Linux laptop.
The exact device path varies between Linux distros if looking to use Terminal.
Find the mount point:

```sh
lsblk
```
