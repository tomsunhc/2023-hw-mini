set(name hello_fifo)

if (TARGET tinyusb_device)
    add_executable(${name} fifo.c)
    target_link_libraries(${name} pico_stdlib pico_multicore)

    # enable usb output, disable uart output
    pico_enable_stdio_usb(${name} 1)
    pico_enable_stdio_uart(${name} 0)

    # create map/bin/hex/uf2 file etc.
    pico_add_extra_outputs(${name})
elseif(PICO_ON_DEVICE)
    message(WARNING "not building ${name} because TinyUSB submodule is not initialized in the SDK")
endif()
