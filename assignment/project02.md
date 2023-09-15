# Project 02 - dual-threaded, dual-response time measurement + light measurement

Have the LED blink at random intervals.
Measure average, minimum, maximum response time for 10 flashes total.
Measure this using two switches, so that either you and a friend, or use two different fingers to see the response times for two different people / fingers.

At the same time, in a separate thread, measure the light intensity as in exercise 04 periodically and log to its own JSON file.
We are not using semaphores or locks (unless you are experienced and really want to), it's just to show we can run two threads at the same time.

Use a JSON file to store the parameters for the experiment as in the prior exercises.

Write the response times to a JSON file along with minimum, maximum, average response time and "score" in number of non-misses vs. total light flashes.

Please include the two JSON files in your repository as downloaded from the Pico.
That is, there are two uploaded JSON files to your Git repository from the Pico:

* "proj2-light.json"
* "proj2-score.json"

(you can name them how you like, just showing there's two distinct files)
