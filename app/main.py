from config import *



# Functions for my CRUD Operations
def add_technical_instructor():
    name = input("Enter Instructor Name: ")
    email = input("Enter Instructor Email: ")
    instructor = TechnicalInstructor(name=name, email=email)
    session.add(instructor)
    session.commit()
    print("Instructor added successfully.")

def view_technical_instructors():
    instructors = session.query(TechnicalInstructor).all()
    for instructor in instructors:
        print(f"{instructor.id} - {instructor.name} - {instructor.email}")

def update_technical_instructor():
    instructor_id = int(input("Enter Instructor ID to update: "))
    instructor = session.query(TechnicalInstructor).filter_by(id=instructor_id).first()
    if instructor:
        instructor.name = input(f"Enter new name (current: {instructor.name}): ")
        instructor.email = input(f"Enter new email (current: {instructor.email}): ")
        session.commit()
        print("Instructor updated successfully.")
    else:
        print("Instructor not found.")

def delete_technical_instructor():
    instructor_id = int(input("Enter Instructor ID to delete: "))
    instructor = session.query(TechnicalInstructor).filter_by(id=instructor_id).first()
    if instructor:
        session.delete(instructor)
        session.commit()
        print("Instructor deleted successfully.")
    else:
        print("Instructor not found.")

# ====================COURSE=========================
def add_course():
    title = input("Enter Course Title: ")
    instructor_id = int(input("Enter Instructor ID: "))
    course = Course(title=title, instructor_id=instructor_id)
    session.add(course)
    session.commit()
    print("Course added successfully.")

def view_courses():
    courses = session.query(Course).all()
    for course in courses:
        print(f"{course.id} - {course.title} - Instructor ID: {course.instructor_id}")

def update_course():
    course_id = int(input("Enter Course ID to update: "))
    course = session.query(Course).filter_by(id=course_id).first()
    if course:
        course.title = input(f"Enter new title (current: {course.title}): ")
        session.commit()
        print("Course updated successfully.")
    else:
        print("Course not found.")

def delete_course():
    course_id = int(input("Enter Course ID to delete: "))
    course = session.query(Course).filter_by(id=course_id).first()
    if course:
        session.delete(course)
        session.commit()
        print("Course deleted successfully.")
    else:
        print("Course not found.")


# ====================STUDENT=========================
def add_student():
    name = input("Enter Student Name: ")
    email = input("Enter Student Email: ")
    course_id = input("Enter the Course ID: ")
    student = Student(name=name, email=email, course_id=course_id)
    session.add(student)
    session.commit()
    print("Student added successfully.")

def view_students():
    students = session.query(Student).all()
    for student in students:
        print(f"{student.id} - {student.name} - {student.email} - {student.course_id}")

def update_student():
    student_id = int(input("Enter Student ID to update: "))
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        student.name = input(f"Enter new name (current: {student.name}): ")
        student.email = input(f"Enter new email (current: {student.email}): ")
        student.course_id = input(f"Enter new Course ID (current: {student.course_id}): ")
        session.commit()
        print("Student updated successfully.")
    else:
        print("Student not found.")

def delete_student():
    student_id = int(input("Enter Student ID to delete: "))
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
        print("Student deleted successfully.")
    else:
        print("Student not found.")



# ======================= Main CLI App ============================
def main():
    while True:
        os.system('clear')
        print("Welcome to Tech School")
        print("1. Manage Technical Instructors")
        print("2. Manage Courses")
        print("3. Manage Students")
        main_menu_choice = input("Enter your Choice: ")

        if main_menu_choice == '1':
            while True:
                os.system('clear')
                print("1. Add Instructor")
                print("2. View Instructors")
                print("3. Update Instructor")
                print("4. Delete Instructor")
                print("5. Back to Main Menu")
                instructor_menu_choice = input("Enter your Choice: ")
                if instructor_menu_choice == '1':
                    add_technical_instructor()
                elif instructor_menu_choice == '2':
                    view_technical_instructors()
                elif instructor_menu_choice == '3':
                    update_technical_instructor()
                elif instructor_menu_choice == '4':
                    delete_technical_instructor()
                elif instructor_menu_choice == '5':
                    break
                input("Press Enter to continue...")
        
        elif main_menu_choice == '2':
            while True:
                os.system('clear')
                print("1. Add Course")
                print("2. View Courses")
                print("3. Update Course")
                print("4. Delete Course")
                print("5. Back to Main Menu")
                course_menu_choice = input("Enter your Choice: ")
                if course_menu_choice == '1':
                    add_course()
                elif course_menu_choice == '2':
                    view_courses()
                elif course_menu_choice == '3':
                    update_course()
                elif course_menu_choice == '4':
                    delete_course()
                elif course_menu_choice == '5':
                    break
                input("Press Enter to continue...")
        
        elif main_menu_choice == '3':
            while True:
                os.system('clear')
                print("1. Add Student")
                print("2. View Students")
                print("3. Update Student")
                print("4. Delete Student")
                print("5. Back to Main Menu")
                student_menu_choice = input("Enter your Choice: ")
                if student_menu_choice == '1':
                    add_student()
                elif student_menu_choice == '2':
                    view_students()
                elif student_menu_choice == '3':
                    update_student()
                elif student_menu_choice == '4':
                    delete_student()
                elif student_menu_choice == '5':
                    break
                input("Press Enter to continue...")

        else:
            print("Invalid choice! Please choose again.")
            input("Press Enter to continue...")


# Call the main function
main()