# Clock
import time
import sys


class Counter:
    def __init__(self, name):
        self.name = name
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

class Clock:

    seconds = Counter("Seconds")
    minutes = Counter("Minutes")
    hours = Counter("Hours")

    def Tick(self):
        time.sleep(1)
        Clock.seconds.increment()

        if Clock.seconds.count >= 60:
            Clock.seconds.reset()
            Clock.minutes.increment()
            if Clock.minutes.count >= 60:
                Clock.minutes.reset()
                Clock.hours.increment()
                if Clock.hours.count >= 12:
                    Clock.reset_clock()

    def reset_clock(self):
        Clock.seconds.reset()
        Clock.minutes.reset()
        Clock.hours.reset()

    def set_clock(self, seconds, minutes, hours):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def read_clock(self):
        sys.stdout.writelines(" \r Current Time: %d:%d:%d" % (Clock.hours.count, Clock.minutes.count, Clock.seconds.count))


clock = Clock()
while True:
    clock.Tick()
    clock.read_clock()