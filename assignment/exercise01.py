"""
This program prints to the Python REPL

It works on MicroPython on the Pico or laptop as we dynamically detect the Python VM.
"""

import sys
import time

is_micropython = sys.implementation.name == "micropython"


def get_params() -> tuple[int, float]:
    """Get the loop count and sleep time from the user."""
    print(f"Running on {sys.platform}")

    print("How many times shall I loop?")
    N: int = int(input())

    print("How long shall I sleep for each loop iteration?")
    sleep_time: float = float(input())

    return N, sleep_time


def total_time(N: int, sleep_time: float) -> float:
    """Calculate the total time in seconds."""

    return N * sleep_time


def time_remaining(i: int, sleep_time: float) -> float:
    """Calculate the time remaining in seconds."""

    return i * sleep_time


if __name__ == "__main__":
    N, sleep_time = get_params()

    t_predict = total_time(N, sleep_time)
    print(f"Total time (predicted, seconds): {t_predict}")

    tic = time.ticks_ms() if is_micropython else time.monotonic()

    for i in range(N):
        print(f"Loop {i} of {N}: Time remaining: {time_remaining(N-i, sleep_time):.3f}")

        time.sleep(sleep_time)

    toc = time.ticks_ms() if is_micropython else time.monotonic()

    t_elapsed = time.ticks_diff(toc, tic) / 1000.0 if is_micropython else toc - tic

    print(f"Total time (measured, predicted) [seconds]: {t_elapsed:.3f} {t_predict:.3f}")
