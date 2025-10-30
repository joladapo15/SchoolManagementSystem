
class Student:
  def __init__(self, name, id ,major , courses):
    self.name = name
    self.student_id = id
    self.major = major
    self.courses = courses

  def to_dict(self):
    return {
      "Name": self.name,
      "ID": self.student_id,
      "Major": self.major,
      "Courses": ",".join(self.courses)
    }

