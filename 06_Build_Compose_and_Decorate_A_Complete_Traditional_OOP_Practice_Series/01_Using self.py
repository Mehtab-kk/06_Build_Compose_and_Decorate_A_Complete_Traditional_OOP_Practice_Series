class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
#   method
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Student Marks: {self.marks}")


student1 = Student("Zainab", 99)
student1.display()
