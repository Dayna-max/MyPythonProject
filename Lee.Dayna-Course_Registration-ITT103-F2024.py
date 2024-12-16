#Define the course class to represent a course in the system.
class Course:
    def __init__(self, course_id, name, fee):
        self.course_id = course_id
        self.name = name
        self.fee = fee
#Starting Course object with course_id,name,fee.`

class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = []
        self.balance = 0

#This block is to enroll a student and update their balance without having duplicate enrollments in the system.
#The raise function basically highlights the error and prompt the system to display and error message.
    def enroll(self, course):
        if course in self.courses:
            raise ValueError("Student is already enrolled in this course.")
        self.courses.append(course)
        self.balance += course.fee

    def get_total_fee(self):
        return sum(course.fee for course in self.courses)

#The registration class is to manage students and courses, which involves list and dictionary
class RegistrationSystem:
    def __init__(self):
        self.courses = []
        self.students = {}

    def add_course(self, course_id, name, fee):
        if any(course.course_id == course_id for course in self.courses):
            raise ValueError("Course with this ID already exists.")
        self.courses.append(Course(course_id, name, fee))

#For this block it registers a new student.
# But if another student is to be registered\ with the same ID the raise function would display an error message
    def register_student(self, student_id, name, email):
        if student_id in self.students:
            raise ValueError("Student with this ID already exists.")
        self.students[student_id] = Student(student_id, name, email)

    def enroll_in_course(self, student_id, course_id):
        if student_id not in self.students:
            raise ValueError("Student not found.")
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if course is None:
            raise ValueError("Course not found.")
        self.students[student_id].enroll(course)

#Here this block calculates or deducts the 40% from the balances from the courses the student is enrolled in.
    def calculate_payment(self, student_id):
        if student_id not in self.students:
            raise ValueError("Student not found.")
        student = self.students[student_id]
        if student.balance * 0.4 > 0:
            student.balance -= student.balance * 0.4
        else:
            raise ValueError("Insufficient balance to process payment.")

    def check_student_balance(self, student_id):
        if student_id not in self.students:
            raise ValueError("Student not found.")
        return self.students[student_id].balance

    def show_courses(self):
        return [(course.course_id, course.name, course.fee) for course in self.courses]

    def show_registered_students(self):
        return [(student.student_id, student.name, student.email) for student in self.students.values()]

    def show_students_in_course(self, course_id):
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if course is None:
            raise ValueError("Course not found.")
        return [student.name for student in self.students.values() if course in student.courses]


def main_menu():
    system = RegistrationSystem()
    while True:
        print("\n1. Add Course")
        print("2. Register Student")
        print("3. Enroll in Course")
        print("4. Calculate Payment")
        print("5. Check Student Balance")
        print("6. Show Courses")
        print("7. Show Registered Students")
        print("8. Show Students in Course")
        print("9. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            fee = float(input("Enter course fee: "))
            try:
                system.add_course(course_id, name, fee)
                print("Course added successfully.")
            except ValueError as e:
                print(e)

        elif choice == '2':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            try:
                system.register_student(student_id, name, email)
                print("Student registered successfully.")
            except ValueError as e:
                print(e)

        elif choice == '3':
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            try:
                system.enroll_in_course(student_id, course_id)
                print("Student enrolled successfully.")
            except ValueError as e:
                print(e)

        elif choice == '4':
            student_id = input("Enter student ID: ")
            try:
                system.calculate_payment(student_id)
                print("Payment processed successfully.")
            except ValueError as e:
                print(e)

        elif choice == '5':
            student_id = input("Enter student ID: ")
            try:
                balance = system.check_student_balance(student_id)
                print(f"Current balance: {balance}")
            except ValueError as e:
                print(e)

        elif choice == '6':
            courses = system.show_courses()
            for course in courses:
                print(course)

        elif choice == '7':
            students = system.show_registered_students()
            for student in students:
                print(student)

        elif choice == '8':
            course_id = input("Enter course ID: ")
            try:
                students_in_course = system.show_students_in_course(course_id)
                print("Students enrolled in course:", students_in_course)
            except ValueError as e:
                print(e)

        elif choice == '9':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
