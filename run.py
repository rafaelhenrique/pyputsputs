# -*- coding: utf-8 -*-
import time

import alsaaudio
import audioop
import pingo

board = pingo.detect.get_board()


def configure_all_pins_out():
    """Configure all pins of board on out mode"""
    for pin in board.pins.values():
        try:
            pin.mode = pingo.OUT
        except:
            pass


def blink(led, time_interval):
    """Blink led by time"""
    led.hi()
    time.sleep(time_interval)
    led.low()


def configure_microphone(rate=44100, channel=1, periodsize=160):
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
    configure_all_pins_out()
    ordered_leds = [board.pins[11], board.pins[10], board.pins[9],
                    board.pins[6], board.pins[5], board.pins[3]]

    maximum = 0
    mic = configure_microphone()
    while True:
        # Read data from device
        l, data = mic.read()
        if l:
            # Return the maximum of the absolute value of all
            # samples in a fragment.
            led = audioop.max(data, 2) / 2100

            # Only one adjust to my microphone
            if led == 7:
                led = 6
            led -= 1
            led = ordered_leds[led]
            blink(led, .002)

        time.sleep(.001)
