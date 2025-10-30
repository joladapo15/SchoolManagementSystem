from SMS_student import Student
from SMS_faculty import Faculty
from SMS_course import Course
from utils_helper import save_to_csv


class SchoolManager:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.faculty = {}

    # Add faculty
    def add_faculty(self, faculty_id, name, department):
        if faculty_id in self.faculty:
            print(f"⚠️ Faculty ID {faculty_id} already exists.")
            return
        self.faculty[faculty_id] = Faculty(faculty_id, name, department)
        print(f"✅ Added faculty: {name}")

    # Add course
    def add_course(self, course_id, name, faculty_id=None):
        if course_id in self.courses:
            print(f"⚠️ Course ID {course_id} already exists.")
            return
        course = Course(course_id, name)
        if faculty_id and faculty_id in self.faculty:
            course.assign_faculty(self.faculty[faculty_id])
        self.courses[course_id] = course
        print(f"✅ Added course: {name}")

    # Add student
    def add_student(self, student_id, name, major, courses=None):
        if student_id not in self.students:
        # Pass courses or empty list
            student = Student(student_id, name, major, courses if courses else [])
            self.students[student_id] = student
            print(f"✅ Added student: {name}")

        # Enroll student in listed courses (if any)
        if courses:
            for course_id in courses:
                if course_id in self.courses:
                    self.enroll_student_in_course(student_id, course_id)
                else:
                    print(f"⚠️ Course {course_id} not found.")
        else:
            print(f"⚠️ Student ID {student_id} already exists.")


    # Enroll student
    def enroll_student_in_course(self, student_id, course_id):
        if student_id not in self.students:
            print(f"⚠️ Student {student_id} not found.")
            return
        if course_id not in self.courses:
            print(f"⚠️ Course {course_id} not found.")
            return
        student = self.students[student_id]
        course = self.courses[course_id]
        student.enroll(course)
        course.enroll_student(student)
        print(f"✅ Enrolled {student.name} in {course.name}")

    # Assign faculty
    def assign_faculty_to_course(self, course_id, faculty_id):
        if course_id not in self.courses:
            print(f"⚠️ Course {course_id} not found.")
            return
        if faculty_id not in self.faculty:
            print(f"⚠️ Faculty {faculty_id} not found.")
            return
        course = self.courses[course_id]
        faculty = self.faculty[faculty_id]
        course.assign_faculty(faculty)
        print(f"✅ Assigned {faculty.name} to {course.name}")

    # List students
    def list_all_students(self):
        print("\n📘 All Students:")
        if not self.students:
            print("No students available.")
            return
        for student in self.students.values():
            courses = ', '.join(c.course_id for c in student.courses) if student.courses else "None"
            print(f"{student.student_id} | {student.name} | {student.major} | Courses: {courses}")

    # List courses
    def list_all_courses_with_faculty(self):
        print("\n📚 All Courses:")
        if not self.courses:
            print("No courses available.")
            return
        for course in self.courses.values():
            faculty_name = course.faculty.name if course.faculty else "Unassigned"
            print(f"{course.course_id} | {course.name} | Faculty: {faculty_name}")

    # Students in a course
    def display_enrolled_students(self, course_id):
        if course_id not in self.courses:
            print(f"⚠️ Course {course_id} not found.")
            return
        course = self.courses[course_id]
        print(f"\n👩‍🎓 Students in {course.name}:")
        if not course.students:
            print("No students enrolled.")
            return
        for student in course.students:
            print(f"{student.student_id} | {student.name}")

    # Save to CSV
    def save_all(self):
        save_to_csv("faculty.csv", [f.to_dict() for f in self.faculty.values()],
                    ["FacultyID", "Name", "Department"])
        save_to_csv("courses.csv", [c.to_dict() for c in self.courses.values()],
                    ["CourseID", "CourseName", "FacultyID"])
        save_to_csv("students.csv", [s.to_dict() for s in self.students.values()],
                    ["StudentID", "Name", "Major", "Courses"])
        print("💾 Data saved!")


# Main Menu
def main_menu():
    school = SchoolManager()

    while True:
        print("\n===== 🎓 SCHOOL MANAGEMENT MENU =====")
        print("1️⃣  List all students")
        print("2️⃣  List all courses with faculty")
        print("3️⃣  View students enrolled in a course")
        print("4️⃣  Add new student")
        print("5️⃣  Add new faculty")
        print("6️⃣  Add new course")
        print("7️⃣  Enroll student in a course")
        print("8️⃣  Assign faculty to a course")
        print("9️⃣  Save and Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            school.list_all_students()
        elif choice == "2":
            school.list_all_courses_with_faculty()
        elif choice == "3":
            cid = input("Enter course ID: ")
            school.display_enrolled_students(cid)
        elif choice == "4":
            sid = input("Student ID: ")
            name = input("Name: ")
            major = input("Major: ")
            courses_input = input("Enter course IDs (comma-separated, optional): ")
            courses = [c.strip() for c in courses_input.split(",") if c.strip()]
            school.add_student(sid, name, major, courses)
        elif choice == "5":
            fid = input("Faculty ID: ")
            name = input("Name: ")
            dept = input("Department: ")
            school.add_faculty(fid, name, dept)
        elif choice == "6":
            cid = input("Course ID: ")
            cname = input("Course name: ")
            fid = input("Assign faculty ID (optional): ").strip()
            school.add_course(cid, cname, fid if fid else None)
        elif choice == "7":
            sid = input("Student ID: ")
            cid = input("Course ID: ")
            school.enroll_student_in_course(sid, cid)
        elif choice == "8":
            cid = input("Course ID: ")
            fid = input("Faculty ID: ")
            school.assign_faculty_to_course(cid, fid)
        elif choice == "9":
            school.save_all()
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")


if __name__ == "__main__":
    main_menu()





