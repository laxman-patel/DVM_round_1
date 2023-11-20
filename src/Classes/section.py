from enum import Enum

class Section:
    def __init__(self, section_type, slot, course):
        self.section_type = section_type 
        self.slot = slot
        self.course = course

    def __str__(self):
        return f"(Section Type: {self.section_type}, Slot: {self.slot}),"

class SectionType(Enum):
    LECTURE = 1
    TUTORIAL = 2
    LAB = 3