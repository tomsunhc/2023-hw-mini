# Miniproject assignment

This assignment uses the Raspberry Pi Pico H (non-W no wireless version) as handed out in class.

Feel free to use AI assistants if you wish such as ChatGPT, GitHub Copilot, etc.
As a software engineer I also use these AI tools, but they regularly make mistakes, sometimes subtle mistakes.

Each student please fork this "2023-hw-mini" repository.
Then `git clone` your forked repository to your local machine as you write your code and results.
The **final submission will be a link to your forked GitHub repository** containing your code and JSON files as specified in the exercises and projects below.
For question responses please make a top-level "Report.md" file in your forked GitHub repository.
If you choose to make your GitHub repository "Private", then you would need to add my GitHub username
[drhirsch](https://github.com/drhirsch)
under Repository Settings as a read-only Collaborator

In this Git repository, the directory
[python/](../python)
contains MicroPython script that flashes the LED while simultaneously reading onboard temperature, demonstrating multi-threading on the dual-core CPU of the Pi Pico.

## Exercises

* [Exercise 01](./exercise01.md)
* [Exercise 02](./exercise02.md)
* [Exercise 03](./exercise03.md)
* [Exercise 04](./exercise04.md)

## Project

[Project 01](./project01.md): single-threaded response-time measurement

[Project 02](./project02.md): dual-threaded response-time measurement

## Summary

This assignment has a few exercises and finally has the student create a multi-threaded Python script to make a response-time measurement where the human presses the tactile switch when they see the LED flash.
Be creative!

This assignment is done in teams of two students.
Each student has their own Pico H, breadboard and circuit components.
Although you can work in your own Git repos, please decide on a single Git repo to have as your final assignment submitted.

## Rubric

Score out of 10 points total:

* 4 points: Exercises 01-04 linked at the top of this page
* 3 points: Project 01: single-threaded response-time measurement
* 3 points: Project 02: dual-threaded response-time measurement
