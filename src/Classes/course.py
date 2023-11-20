class Course: 
    def __init__(self, course_name, exam_date, prof_name, course_units):
        self.course_name = course_name
        self.exam_date = exam_date
        self.prof_name = prof_name
        self.course_units = course_units
        self.sections = []
    
    def get_all_sections(self):
        return self.sections
    
    def __str__(self):
        return f"Course: {self.course_name}, Exam Date: {self.exam_date}, Prof Name: {self.prof_name}, Course Units: {self.course_units}, Sections: {'  '.join([str(section) for section in self.sections])}"

    def populate_section(self,section):
        self.sections.append(section)