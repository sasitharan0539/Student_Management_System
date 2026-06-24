# Student_Management_System
basic level of AIML
# Student Management System

## Project Overview

The Student Management System is a Python-based console application that helps manage student records efficiently. It allows users to add, view, search, update, and delete student information. The system also manages student marks, attendance, and generates reports.

This project was developed as a Phase-1 Python project to learn core programming concepts such as functions, dictionaries, loops, conditional statements, file handling, and JSON storage.

---

## Features

### Add Student
Store student details including:
- Student ID
- Name
- Age
- Department
- Year
- Email
- Phone Number

### View Students
Display all student records in a structured format.

### Search Student
Search student details using Student ID.

### Update Student
Update:
- Name
- Email
- Phone Number
- Department

### Delete Student
Delete a student record using Student ID.

### Marks Management
Store marks for:
- Mathematics
- Python
- DBMS
- AI Basics

Calculate:
- Total Marks
- Percentage
- Grade

### Attendance Management
Store:
- Total Classes
- Attended Classes

Calculate:
- Attendance Percentage

### Top Performer Report
Find the student with the highest percentage.

### JSON File Storage
Save and load student data using a JSON file (`students.json`).

---

## Technologies Used

- Python 3
- JSON File Handling
- Dictionaries
- Functions
- Loops
- Conditional Statements

---

## Project Structure

```text
Student_Management_System/
│
├── main.py
├── students.json
├── README.md
└── screenshots/
```

---

## How to Run

### 1. Install Python

Download Python from:

https://www.python.org/downloads/

Check installation:

```bash
python --version
```

### 2. Create Project Files

```text
main.py
students.json
README.md
```

### 3. Initialize JSON File

Create `students.json` and add:

```json
{}
```

### 4. Run the Program

```bash
python main.py
```

---

## Menu Options

```text
===== STUDENT MANAGEMENT SYSTEM =====

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Marks Report
7. Attendance Report
8. Top Performer
9. Exit
```

---

## Sample Usage

### Add Student

```text
Enter Student ID: 101
Enter Name: Arun Kumar
Enter Age: 20
Enter Department: CSE
Enter Year: 3
Enter Email: arun@gmail.com
Enter Phone Number: 9876543210
```

### Search Student

```text
Enter Student ID: 101

Student Found
Name: Arun Kumar
Department: CSE
Year: 3
```

### Marks Report

```text
Total Marks: 350
Percentage: 87.5
Grade: B
```

### Attendance Report

```text
Attendance Percentage: 92.0 %
```

---

## Learning Outcomes

This project helped in understanding:

- Variables and Data Types
- Functions
- Dictionaries and Nested Dictionaries
- Loops and Conditional Statements
- JSON File Handling
- Menu-Driven Applications
- Data Storage and Retrieval

---

## Future Enhancements

- Admin Login System
- Automatic Student ID Generation
- Search by Department
- Student Ranking System
- Export to CSV
- GUI using Tkinter
- MySQL Database Integration

---

## Author

**Name:** Sasi

**Department:** Artificial Intelligence and Machine Learning (AIML)

**Project:** Phase-1 Python Project

---
