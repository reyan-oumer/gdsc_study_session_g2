student_database = {}

def add_student():
    name = input("Enter your full name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender: (M/F) ")
    grade = input("Enter your grade: ")
    city = input("Enter your city: ")
    
    student_database[name] = {'age': age,'gender': gender, 'grade': grade, 'city': city}
    print("Student added successfully!")

def view_student():
    name = input("Enter student's full name to view details: ")
    if name in student_database:
        print(f"Name: {name}, Age: {student_database[name]['age']}, Gender: {student_database[name]['gender']},Grade: {student_database[name]['grade']},City: {student_database[name]['city']}")
    else:
        print("Student not found in the database.")

def list_all_students():
    print("List of all students in the database:")
    for name, details in student_database.items():
        print(f"Name: {name}, Age: {details['age']}, Gender: {details['gender']}, Grade: {details['grade']}, City: {details['city']}")

def update_student():
    name = input("Enter student's full name to update details: ")
    if name in student_database:
        new_age = input("Enter new age: ")
        new_grade = input("Enter new grade: ")
        new_city = input("Enter new city: ")
        
        student_database[name]['age'] = new_age
        student_database[name]['grade'] = new_grade
        student_database[name]['city'] = new_city
        print("Student information updated successfully!")
    else:
        print("Student not found in the database.")

def delete_student():
    name = input("Enter your name to delete from the database: ")
    if name in student_database:
        del student_database[name]
        print("Student deleted successfully!")
    else:
        print("Student not found in the database.")


while True:
    print("\nWelcome to the Student Database Program")
    print("1. Add Student")
    print("2. View Student")
    print("3. List All Students")
    print("4. Update Student Information")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_student()
    elif choice == '3':
        list_all_students()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
