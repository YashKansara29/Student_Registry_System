#featuring Object-Oriented Design, persistent JSON storage, and comprehensive error handling for secure data management.
import json
import os

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "marks": self.marks
        }
class StudentRegistry:
    def __init__(self, filename):
        self.filename = filename
        self.students = []
        self.load_students()
    def add_student(self, student):
        self.students.append(student)
        self.save_students()
    def save_students(self):
        with open(self.filename, "w") as f:
            json.dump([student.to_dict() for student in self.students], f, indent=4)
    def load_students(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    self.students = [Student(**student) for student in data]
            except json.JSONDecodeError:
                print("Error: The file contains invalid JSON.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
    def display_students(self):
        for student in self.students:
            print(f"Name: {student.name}, Age: {student.age}, Marks: {student.marks}")
# Example usage
registry = StudentRegistry("students.json")
registry.add_student(Student("Yash", 22, 94))
registry.add_student(Student("Rutul", 21, 88))
registry.display_students()
