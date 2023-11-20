from datetime import time
from enum import Enum

class Slot:
    def __init__(self, day, start_time, end_time):
        self.day = day
        self.start_time = time(*map(int, start_time.split(':')))
        self.end_time = time(*map(int, end_time.split(':')))

    def check_clash(self, other_slot):
        print(self.day, other_slot.day)
        
        if self.day != other_slot.day:
            return False

        return not (self.end_time <= other_slot.start_time or self.start_time >= other_slot.end_time)

    def __str__(self):
        return f"(Day: {self.day}, Start Time: {self.start_time}, End Time: {self.end_time})"

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6