students = []


# =========================
# Helper Functions
# =========================

def calculate_total(marks):
    return sum(marks.values())


def calculate_percentage(total, subjects):
    return total / subjects


def find_student(roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            return student
    return None


# =========================
# Add Student
# =========================

def add_student():
    try:
        roll_no = int(input("Enter Roll Number: "))

        if roll_no <= 0:
            print("Roll number must be positive.")
            return

        # Check duplicate
        if find_student(roll_no):
            print("Student already exists.")
            return

        name = input("Enter Name: ").strip()
        age = int(input("Enter Age: "))
        grade = input("Enter Class/Grade: ").strip()

        if age < 5 or age > 100:
            print("Invalid age.")
            return

        math = float(input("Enter Math Marks: "))
        physics = float(input("Enter Physics Marks: "))
        chemistry = float(input("Enter Chemistry Marks: "))

        # Validate marks
        marks_list = [math, physics, chemistry]

        for mark in marks_list:
            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100.")
                return

        marks = {
            "Math": math,
            "Physics": physics,
            "Chemistry": chemistry
        }

        total = calculate_total(marks)
        percentage = calculate_percentage(total, 3)

        student = {
            "roll_no": roll_no,
            "name": name,
            "age": age,
            "grade": grade,
            "marks": marks,
            "total": total,
            "percentage": percentage
        }

        students.append(student)

        print("Student added successfully.")

    except ValueError:
        print("Invalid input.")


# =========================
# View Students
# =========================

def view_students():

    if not students:
        print("No records found.")
        return

    print("\n" + "=" * 90)

    print(f"{'Roll':<10}{'Name':<20}{'Age':<10}{'Grade':<15}{'Total':<10}{'Percent':<10}")

    print("=" * 90)

    for student in students:
        print(
            f"{student['roll_no']:<10}"
            f"{student['name']:<20}"
            f"{student['age']:<10}"
            f"{student['grade']:<15}"
            f"{student['total']:<10}"
            f"{student['percentage']:.2f}%"
        )

    print("=" * 90)


# =========================
# Search Student
# =========================

def search_student():
    try:
        roll_no = int(input("Enter Roll Number to Search: "))

        student = find_student(roll_no)

        if student:
            print("\nStudent Found")
            print("-" * 30)

            print(f"Roll No : {student['roll_no']}")
            print(f"Name    : {student['name']}")
            print(f"Age     : {student['age']}")
            print(f"Grade   : {student['grade']}")
            print(f"Marks   : {student['marks']}")
            print(f"Total   : {student['total']}")
            print(f"Percent : {student['percentage']:.2f}%")

        else:
            print("Student not found.")

    except ValueError:
        print("Invalid input.")


# =========================
# Update Marks
# =========================

def update_marks():

    try:
        roll_no = int(input("Enter Roll Number: "))

        student = find_student(roll_no)

        if not student:
            print("Student not found.")
            return

        print("Enter new marks:")

        math = float(input("Math: "))
        physics = float(input("Physics: "))
        chemistry = float(input("Chemistry: "))

        marks_list = [math, physics, chemistry]

        for mark in marks_list:
            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100.")
                return

        student["marks"] = {
            "Math": math,
            "Physics": physics,
            "Chemistry": chemistry
        }

        student["total"] = calculate_total(student["marks"])

        student["percentage"] = calculate_percentage(
            student["total"],
            3
        )

        print("Marks updated successfully.")

    except ValueError:
        print("Invalid input.")


# =========================
# Delete Student
# =========================

def delete_student():

    try:
        roll_no = int(input("Enter Roll Number: "))

        student = find_student(roll_no)

        if not student:
            print("Student not found.")
            return

        confirm = input("Are you sure? (Y/N): ").upper()

        if confirm == "Y":
            students.remove(student)
            print("Student deleted successfully.")
        else:
            print("Deletion cancelled.")

    except ValueError:
        print("Invalid input.")


# =========================
# Main Menu
# =========================

def main():

    while True:

        print("\n")
        print("=" * 40)
        print(" STUDENT RECORD MANAGEMENT SYSTEM ")
        print("=" * 40)

        print("1. Add Student Record")
        print("2. View All Records")
        print("3. Search Student by Roll Number")
        print("4. Update Student Marks")
        print("5. Delete Student Record")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice (1-6): "))

            if choice == 1:
                add_student()

            elif choice == 2:
                view_students()

            elif choice == 3:
                search_student()

            elif choice == 4:
                update_marks()

            elif choice == 5:
                delete_student()

            elif choice == 6:
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a number.")


# =========================
# Program Start
# =========================

main()