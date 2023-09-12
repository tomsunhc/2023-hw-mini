"""
Morse Code decoder

based on https://github.com/printnplay/Pico-MicroPython/blob/main/MorseCodeCreator.py
"""

from machine import Pin
import time
import json
import os

# Create a dictionary of Morse Code. s is for Short (or dots), l is for Long (or dashes)
MorseCodes = {
    " ": "",
    "a": "sl",
    "b": "lsss",
    "c": "lsls",
    "d": "lss",
    "e": "s",
    "f": "ssls",
    "g": "lls",
    "h": "ssss",
    "i": "ss",
    "j": "slll",
    "k": "lsl",
    "l": "slss",
    "m": "ll",
    "n": "ls",
    "o": "lll",
    "p": "slls",
    "q": "llsl",
    "r": "sls",
    "s": "sss",
    "t": "l",
    "u": "ssl",
    "v": "sssl",
    "w": "sll",
    "x": "lssl",
    "y": "lsll",
    "z": "llss",
    "1": "sllll",
    "2": "sslll",
    "3": "sssll",
    "4": "ssssl",
    "5": "sssss",
    "6": "lssss",
    "7": "llsss",
    "8": "lllss",
    "9": "lllls",
    "0": "lllll",
}


def get_params(param_file: str) -> dict:
    """Reads parameters from a JSON file."""

    if not is_regular_file(param_file):
        raise OSError(f"File {param_file} not found")

    with open(param_file) as f:
        params = json.load(f)

    return params


def is_regular_file(path: str) -> bool:
    """Checks if a regular file exists."""

    S_IFREG = 0x8000

    try:
        return os.stat(path)[0] & S_IFREG != 0
    except OSError:
        return False


def letterlookup(stringvalue: str) -> str:
    for k in MorseCodes:
        if MorseCodes[k] == stringvalue:
            return k
    return " "


def blinkletter(letter: str, params: dict) -> None:
    """blink LED Morse code letters"""

    led = machine.Pin("LED", machine.Pin.OUT)

    if letter != "":
        currentletter = MorseCodes[letter]
    if letter == " ":
        time.sleep(params["inter_letter_ms"] / 1000.0)
        return

    print(letter + " : " + currentletter)
    for c in currentletter:
        if c == "l":
            blinkspeed = params["blink_slow_ms"] / 1000.0
        if c == "s":
            blinkspeed = params["blink_fast_ms"] / 1000.0

        led.high()
        time.sleep(blinkspeed)
        led.low()
        time.sleep(blinkspeed)

    time.sleep(0.6)


def play(message: str, params: dict) -> None:
    for c in message:
        blinkletter(str.lower(c), params)


def record(params: dict) -> str:
    """capture morse code message from button presses
    we show via the LED the button presses as captured.
    This can help illustrate issues over sample time being too large
    """

    led = machine.Pin("LED", machine.Pin.OUT)
    button = Pin(16, Pin.IN, Pin.PULL_UP)
    letter = ""
    word = ""
    count = 0

    exit_threshold_ms = params["exit_threshold_ms"]
    dot_dash_threshold_ms = params["dot_dash_threshold_ms"]
    Tsample = params["sample_ms"] / 1000.0

    print(f"tap Morse Code message! Wait {exit_threshold_ms / 1000.} seconds to exit")

    tic_char = time.ticks_ms()

    while True:
        if button.value() == 0:
            # Button being pressed
            if count == 0:
                tic_char = time.ticks_ms()
            count += 1
            led.high()
        else:
            toc = time.ticks_ms()
            tdiff = time.ticks_diff(toc, tic_char)
            led.low()
            # Button released, measure if dot or dash
            if count > 0:
                if tdiff < dot_dash_threshold_ms:
                    letter += "s"
                else:
                    letter += "l"
            count = 0

            if tdiff > 3 * dot_dash_threshold_ms:
                if letter != "":
                    word += letterlookup(letter)
                    letter = ""
                    print(word)

            if tdiff > exit_threshold_ms:
                print("You recorded " + word)
                print("Exiting recording mode")

                return word

        time.sleep(Tsample)


if __name__ == "__main__":
    params = get_params("exercise03.json")

    # %% play wakeup hello message
    play("hello", params)

    # %% record and playback message
    play(record(params), params)
