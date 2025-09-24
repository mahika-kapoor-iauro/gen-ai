class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, grade):
        if student_id in self.students:
            print("Student ID already exists.")
        else:
            self.students[student_id] = Student(student_id, name, age, grade)
            print("Student added successfully.")

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student removed successfully.")
        else:
            print("Student ID not found.")

    def get_student(self, student_id):
        return self.students.get(student_id, None)

    def list_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students.values():
                print(student)

# Example usage:
if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.add_student(1, "Alice", 20, "A")
    sms.add_student(2, "Bob", 21, "B")
    sms.list_students()
    sms.remove_student(1)
    sms.list_students()