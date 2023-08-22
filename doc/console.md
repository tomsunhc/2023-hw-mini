# USB console

The USB console (if used by your program) uses the TinyUSB library.
CMake must be configured as in the
[hello_usb](./src/hello_usb/CMakeLists.txt)
to enable USB and disable UART for the particular target.
Each operating system has a distinct way of accessing USB-serial gateways:

* Windows: look in Device Manager under Ports-there should be COM* device. Use [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) to connect at 115200 baud serial
* Linux: look under /dev/ttyACM* and connect with PuTTY or `screen /dev/ttyACM0 115200`
* macOS: look under "/dev/cu.usbserial" and connect with PuTTY `brew install putty` or `screen /dev/cu.usbserial 115200`
