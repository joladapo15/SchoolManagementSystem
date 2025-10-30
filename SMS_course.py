class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.faculty = None
        self.students = []

    def assign_faculty(self, faculty):
        """Assign a faculty member to this course."""
        self.faculty = faculty

    def enroll_student(self, student):
        """Enroll a student in this course."""
        if student not in self.students:
            self.students.append(student)
        else:
            print(f"{student.name} is already enrolled in {self.name}.")

    def to_dict(self):
        """Convert course details to a dictionary for saving to CSV."""
        faculty_id = self.faculty.faculty_id if self.faculty else "None"
        return {
            "CourseID": self.course_id,
            "CourseName": self.name,
            "FacultyID": faculty_id
        }




    