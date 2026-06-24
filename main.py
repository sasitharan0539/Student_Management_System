
import json

# =========================
# Global Dictionary
# =========================

students = {}


# =========================
# File Handling Functions
# =========================

def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def load_data():
    global students

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

            # Convert JSON string keys back to integers
            students = {
                int(k): v for k, v in students.items()
            }

    except FileNotFoundError:
        students = {}


# =========================
# Add Student
# =========================

def add_student():

    student_id = int(input("Enter Student ID: "))

    if student_id in students:
        print("Student ID already exists!")
        return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    year = int(input("Enter Year: "))
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")

    print("\nEnter Marks")

    maths = int(input("Mathematics: "))
    python_mark = int(input("Python: "))
    dbms = int(input("DBMS: "))
    ai = int(input("AI Basics: "))

    print("\nEnter Attendance")

    total_classes = int(input("Total Classes: "))
    attended_classes = int(input("Attended Classes: "))

    students[student_id] = {
        "name": name,
        "age": age,
        "department": department,
        "year": year,
        "email": email,
        "phone": phone,

        "marks": {
            "maths": maths,
            "python": python_mark,
            "dbms": dbms,
            "ai": ai
        },

        "attendance": {
            "total": total_classes,
            "attended": attended_classes
        }
    }

    save_data()

    print("\nStudent Added Successfully!")


# =========================
# View Students
# =========================

def view_students():

    if not students:
        print("No students found.")
        return

    print("\n===== STUDENT RECORDS =====")

    for sid, details in students.items():

        print("-" * 40)
        print("ID:", sid)
        print("Name:", details["name"])
        print("Age:", details["age"])
        print("Department:", details["department"])
        print("Year:", details["year"])
        print("Email:", details["email"])
        print("Phone:", details["phone"])

    print("-" * 40)


# =========================
# Search Student
# =========================

def search_student():

    student_id = int(input("Enter Student ID: "))

    if student_id in students:

        student = students[student_id]

        print("\n===== STUDENT FOUND =====")

        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Department:", student["department"])
        print("Year:", student["year"])
        print("Email:", student["email"])
        print("Phone:", student["phone"])

    else:
        print("Student Not Found.")


# =========================
# Update Student
# =========================

def update_student():

    student_id = int(input("Enter Student ID: "))

    if student_id in students:

        students[student_id]["name"] = input("New Name: ")
        students[student_id]["email"] = input("New Email: ")
        students[student_id]["phone"] = input("New Phone: ")
        students[student_id]["department"] = input("New Department: ")

        save_data()

        print("Student Updated Successfully!")

    else:
        print("Student Not Found.")


# =========================
# Delete Student
# =========================

def delete_student():

    student_id = int(input("Enter Student ID: "))

    if student_id in students:

        del students[student_id]

        save_data()

        print("Student Deleted Successfully!")

    else:
        print("Student Not Found.")


# =========================
# Marks Report
# =========================

def marks_report():

    student_id = int(input("Enter Student ID: "))

    if student_id not in students:
        print("Student Not Found.")
        return

    marks = students[student_id]["marks"]

    total = sum(marks.values())

    percentage = total / 4

    if percentage >= 90:
        grade = "A"

    elif percentage >= 75:
        grade = "B"

    elif percentage >= 60:
        grade = "C"

    else:
        grade = "D"

    print("\n===== MARKS REPORT =====")

    print("Total Marks:", total)
    print("Percentage:", round(percentage, 2))
    print("Grade:", grade)


# =========================
# Attendance Report
# =========================

def attendance_report():

    student_id = int(input("Enter Student ID: "))

    if student_id not in students:
        print("Student Not Found.")
        return

    attendance = students[student_id]["attendance"]

    total = attendance["total"]
    attended = attendance["attended"]

    percentage = (attended / total) * 100

    print("\n===== ATTENDANCE REPORT =====")
    print("Attendance Percentage:", round(percentage, 2), "%")


# =========================
# Top Performer
# =========================

def top_performer():

    if not students:
        print("No student records available.")
        return

    highest_percentage = 0
    topper_name = ""

    for details in students.values():

        marks = details["marks"]

        percentage = sum(marks.values()) / 4

        if percentage > highest_percentage:
            highest_percentage = percentage
            topper_name = details["name"]

    print("\n===== TOP PERFORMER =====")
    print("Student Name:", topper_name)
    print("Percentage:", round(highest_percentage, 2))


# =========================
# Main Program
# =========================

load_data()

while True:

    print("\n")
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Marks Report")
    print("7. Attendance Report")
    print("8. Top Performer")
    print("9. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        marks_report()

    elif choice == "7":
        attendance_report()

    elif choice == "8":
        top_performer()

    elif choice == "9":
        save_data()
        print("Thank You!")
        break

    else:
        print("Invalid Choice. Please try again.")
