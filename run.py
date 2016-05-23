# -*- coding: utf-8 -*-
import time
import sys

import alsaaudio
import audioop
import pingo

try:
    print("Loading board...")
    board = pingo.detect.get_board()
    print("Its ok...")
except Exception as e:
    print("Error on get_board: {}".format(e))
    sys.exit(1)


def mode_pins_out(pins):
    """Configure pins mode to out"""
    for pin in pins:
        try:
            pin.mode = pingo.OUT
        except:
            pass


def blink(led, time_interval):
    """Blink led by time"""
    led.hi()
    time.sleep(time_interval)
    led.low()


def blink_leds(leds, time_interval=.0001):
    """Hi leds by time"""
    for led in leds:
        led.hi()
    for led in leds:
        led.lo()


def microphone(rate=44100, channel=1, periodsize=160):
    # Open the device in nonblocking capture mode. The last argument could
    # just as well have been zero for blocking mode. Then we could have
    # left out the sleep call in the bottom of the loop
    mic = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK)

    # Set attributes: Mono, 44100 Hz, 16 bit little endian samples
    mic.setchannels(channel)
    mic.setrate(rate)
    mic.setformat(alsaaudio.PCM_FORMAT_S16_LE)

    # The period size controls the internal number of frames per period.
    # The significance of this parameter is documented in the ALSA api.
    # For our purposes, it is suficcient to know that reads from the device
    # will return this many frames. Each frame being 2 bytes long.
    # This means that the reads below will return either 320 bytes of data
    # or 0 bytes of data. The latter is possible because we are in nonblocking
    # mode.
    mic.setperiodsize(periodsize)
    return mic

if __name__ == "__main__":
    ordered_leds = [board.pins[11], board.pins[10], board.pins[9],
                    board.pins[6], board.pins[5], board.pins[3]]
    mode_pins_out(ordered_leds)

    mic = microphone()
    while True:
        l, data = mic.read()
        if l:
            # if wave of max is 32 this is works
            # if not, you need recalibrate mic
            wave = audioop.max(data, 2) / 1000
            led_index = wave / 6.

            if led_index > 5:
                blink_leds(ordered_leds)
                print("#" * 6)
            elif 5 > led_index > 4:
                blink_leds(ordered_leds[0:5])
                print("#" * 5)
            elif 4 > led_index > 3:
                blink_leds(ordered_leds[0:4])
                print("#" * 4)
            elif 3 > led_index > 2:
                blink_leds(ordered_leds[0:3])
                print("#" * 3)
            elif 2 > led_index > 1:
                blink_leds(ordered_leds[0:2])
                print("#" * 2)
            elif 1 > led_index > 0:
                blink_leds(ordered_leds[0:1])
                print("#" * 1)
