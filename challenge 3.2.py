class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa
def sort_students(student_list):
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students
students = [
Student ("Mathumitha","22UCS15",9.4),
Student ("Dear","22UCS088",9.4),
Student ("kani","22UCS97",9.2),
Student ("anbar","22UCS67",9.1) 
]
sorted_students = sort_students(students)
for student in sorted_students:
  print("name:{},roll Number:{},CGPA:{}".format(student.name,
student.roll_number,
             student.cgpa))