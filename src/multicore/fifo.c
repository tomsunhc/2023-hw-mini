/* https://www.raspberrypi.com/documentation/pico-sdk/high_level.html#pico_multicore */
/* the LED flashing helps see what's happening--the program ends quickly so if you don't
connect immediately on poweron, you won't see the text print. */

#include <stdio.h>
#include "pico/stdlib.h"
#include "pico/multicore.h"

#define FLAG_VALUE 123


void blink(uint32_t, uint32_t);

void blink(uint32_t n, uint32_t delay_ms){
    /* blink onboard LED on/off "n" times with delay "delay_ms" */

    const uint LED_PIN = PICO_DEFAULT_LED_PIN;
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);

    for (int i = 0; i < n; i++)
    {
        gpio_put(LED_PIN, 1);
        sleep_ms(delay_ms);
        gpio_put(LED_PIN, 0);
        sleep_ms(delay_ms);
    }

}

void core1_entry() {

    multicore_fifo_push_blocking(FLAG_VALUE);

    uint32_t g = multicore_fifo_pop_blocking();

    if (g != FLAG_VALUE)
        printf("Hmm, that's not right on core 1!\n");
    else
        printf("Its all gone well on core 1!");

    while (1)
        tight_loop_contents();
}


int main() {
    stdio_init_all();

    printf("Hello, multicore!\n");
    blink(2, 250);

    multicore_launch_core1(core1_entry);

    // Wait for it to start up
    blink(3, 350);
    uint32_t g = multicore_fifo_pop_blocking();

    if (g != FLAG_VALUE){
        printf("Hmm, that's not right on core 0!\n");
        blink(20, 500);
    } else {
        multicore_fifo_push_blocking(FLAG_VALUE);
        printf("It's all gone well on core 0!");
        blink(3, 150);
    }

    return 0;
}
