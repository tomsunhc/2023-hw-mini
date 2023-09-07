# Miniproject assignment

This assignment uses the Raspberry Pi Pico H (non-W no wireless version) as handed out in class.

In this Git repository, the directory
[python/](./python)
contains MicroPython script that flashes the LED while simultaneously reading onboard temperature, demonstrating multi-threading on the dual-core CPU of the Pi Pico.

## Summary

This assignment has the student create a multithreaded Python script to make a response-time measurement where the human presses the tactile switch when they see the LED flash.
Be creative!
The light sensor should also be part of the measurement, captured at/near the same time as the button press.

Please start by doing this without multithreading--just a single for loop perhaps.
When you're comfortable with the measurement, then add the multithreading.
There is no specific "right" answer, as the point is to be creative in learning how to use a microprocessor sensing system.
I would suggest using MicroPython for simplicity, but if you prefer C/C++ with the Pico SDK that is also fine--it's your choice.

This assignment is done in teams of two students.
Each student has their own Pico H, breadboard and circuit components.
Although you can work in your own Git repos, please decide on a single Git repo to have as your final assignment submitted.

## Rubric

Score out of 10 points total:

* 5 points: create / modify a MicroPython (or C/C++ with Pico SDK) program that measures the response time of a human to a flashing LED in a for loop (no multithreading). Log the reponse time data to a file. There may be accuracy issues, part of the discovery is to see what works and what doesn't.
* 3 points: modify to use multithreading and upload measurements to allow comparing original program vs. your modified program
* 2 points: brief report (1-2 paragraphs + measurements) uploaded to your Github repo as Report.md (markdown text file)

