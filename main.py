# Student Registration System

def show_menu():
    print("\n*** Student Registration System ***")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

def add_student(students):
    enrollment_no = input("Enter Student Enrollment Number: ")
    if enrollment_no in students:
        print("Student Enrollment Number already exists!")
        return
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Course Enrolled: ")
    students[enrollment_no] = {"Name": name, "Age": age, "Course": course}
    print("Student added successfully!")

def view_students(students):
    if not students:
        print("No students registered yet!")
        return
    print("\n*** Registered Students ***")
    for enrollment_no, details in students.items():
        print(f"Enrollment No: {enrollment_no}, Name: {details['Name']}, Age: {details['Age']}, Course: {details['Course']}")

def update_student(students):
    enrollment_no = input("Enter Student Enrollment Number to update: ")
    if enrollment_no not in students:
        print("Student not found!")
        return
    print(f"Current Details: {students[enrollment_no]}")
    name = input("Enter New Name (leave blank to keep current): ") or students[enrollment_no]["Name"]
    age = input("Enter New Age (leave blank to keep current): ") or students[enrollment_no]["Age"]
    course = input("Enter New Course (leave blank to keep current): ") or students[enrollment_no]["Course"]
    students[enrollment_no] = {"Name": name, "Age": age, "Course": course}
    print("Student details updated successfully!")

def delete_student(students):
    enrollment_no = input("Enter Student Enrollment Number to delete: ")
    if enrollment_no not in students:
        print("Student not found!")
        return
    del students[enrollment_no]
    print("Student deleted successfully!")

def search_student(students):
    if not students:
        print("No students registered yet!")
        return

    print("\nSearch by:")
    print("1. Enrollment Number")
    print("2. Name")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        enrollment_no = input("Enter Student Enrollment Number: ")
        if enrollment_no in students:
            details = students[enrollment_no]
            print(f"\nDetails for Enrollment No {enrollment_no}:")
            print(f"Name: {details['Name']}, Age: {details['Age']}, Course: {details['Course']}")
        else:
            print("No student found with this Enrollment Number.")
    elif choice == "2":
        name = input("Enter Student Name: ").lower()
        found = False
        for enrollment_no, details in students.items():
            if details["Name"].lower() == name:
                print(f"\nDetails for Enrollment No {enrollment_no}:")
                print(f"Name: {details['Name']}, Age: {details['Age']}, Course: {details['Course']}")
                found = True
        if not found:
            print("No student found with this Name.")
    else:
        print("Invalid choice. Please try again.")

def main():
    students = {}
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            search_student(students)
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
