# refs:
#  https://github.com/raspberrypi/pico-micropython-examples/blob/master/multicore/multicore.py
#  https://github.com/raspberrypi/pico-micropython-examples/blob/master/adc/temperature.py
#  https://docs.micropython.org/en/latest/library/_thread.html

import time
import _thread
import machine
import utime


def led_task(n: int, delay: float) -> None:
    """
    flash the onboard LED "n" times with "delay" seconds between each flash
    """
    led = machine.Pin("LED", machine.Pin.OUT)
    for _ in range(n):
        led.high()
        time.sleep(delay)
        led.low()
        time.sleep(delay)
    print("LED task done")


def sensor_task(n: int, delay: float) -> None:
    """
    read the onboard temperature sensor

    The temperature sensor measures the Vbe voltage of a biased bipolar diode,
    connected to the fifth ADC channel
    Typically, Vbe = 0.706V at 27 degrees C,
    with a slope of -1.721mV (0.001721) per degree.
    """
    sensor_temp = machine.ADC(4)
    conversion_factor = 3.3 / (65535)

    for i in range(n):
        reading = sensor_temp.read_u16() * conversion_factor
        temperature = 27 - (reading - 0.706) / 0.001721
        print(f"{i:02d}:  {temperature:.2f} C")
        utime.sleep(delay)
    print("Sensor task done")


# main program
_thread.start_new_thread(led_task, (10, 0.5))
sensor_task(10, 0.5)
