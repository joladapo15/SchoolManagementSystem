class Faculty:
    def __init__(self, faculty_id, name, department):
        self.faculty_id = faculty_id
        self.name = name
        self.department = department
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)

    def to_dict(self):
        return {
            "FacultyID": self.faculty_id,
            "Name": self.name,
            "Department": self.department
        }

    def __str__(self):
        return f"{self.name} (ID: {self.faculty_id})"
