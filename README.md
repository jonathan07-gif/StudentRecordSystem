# StudentRecordSystem

A small Python CLI app to manage student records (create, view, search, update mentally via files, delete by editing CSV).  
This version uses different file names and structure than the original SBIMS.

## Run
1. Open terminal in project root
2. python app.py

CSV path: `data/students.csv` (header: student_id,full_name,department,year,gpa,contact)

## Features
- Create record
- View all records
- Search students by name
- Filter by department
- Top N students by GPA
- Department counts and average GPA
