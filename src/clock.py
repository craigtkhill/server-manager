import time
import random


class Clock:
    def __init__(self):
        self.time = 0

    def tick(self, unit=1):
        # time.sleep(unit)
        self.time += unit

    def tick_random(self, lower_bound, upper_bound):
        unit = random.randint(lower_bound, upper_bound)
        # time.sleep(unit)
        self.time += unit

    def get_time(self):
        return self.time

    def reset(self):
        self.time = 0
