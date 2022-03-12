"""Clock on Exercism's Python Track"""

import math


class Clock:
    def __init__(self, hour, minute):
        self.hour = (hour + math.floor(minute / 60)) % 24
        self.minute = minute % 60

    def __repr__(self):
        return f'{self.__class__.__name__}({self.hour}, {self.minute})'

    def __str__(self):
        return f'{self.hour:02}:{self.minute:02}'

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    def __add__(self, minutes):
        return self.__class__(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return self.__class__(self.hour, self.minute - minutes)
