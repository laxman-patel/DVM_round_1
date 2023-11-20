import csv

class Timetable:
    def __init__(self):
        self.courses = []
    
    def enroll_course(self, course):
       return self.courses.append(course)

    def check_clashes(self):
        
        for course in self.courses:
            sections = course.get_all_sections()
        
            for i in range(len(sections)):
                for j in range(i+1, len(sections)):
                    if sections[i].slot.check_clash(sections[j].slot):
                        return True
        
        return False
    
    def export_to_csv(self, filename):

        is_course_or_section = input("Do you want to export the courses or sections? type Y for courses and N for sections (Y/N): ")

        if is_course_or_section == 'Y':
            with open(filename, 'w') as csv_file:
                writer = csv.writer(csv_file)

                writer.writerow(['Course Name', 'Exam Date', 'Professor Name', 'Course Units'])


                for course in self.courses:
                    writer.writerow([course.course_name, course.exam_date, course.prof_name, course.course_units])

        elif is_course_or_section == 'N':
            with open(filename, 'w') as csv_file:
                writer = csv.writer(csv_file)

                writer.writerow(['Course Name', 'Section Type', 'Day', 'Start Time', 'End Time'])

                for course in self.courses:
                    for section in course.get_all_sections():
                        writer.writerow([course.course_name, section.section_type, section.slot.day, section.slot.start_time, section.slot.end_time])
        else :
            print("Invalid input")
            return
