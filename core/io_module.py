# core/io_module.py
from core.pupil import Pupil
from core.db import append_pupil, load_all

def create_record_interactive():
    print("Enter new student details:")
    sid = input("Student ID: ").strip()
    existing = [p.sid for p in load_all()]
    if sid in existing:
        print("This ID already exists. Use update instead.")
        return
    full_name = input("Full name: ").strip()
    department = input("Department: ").strip()
    year = input("Year (number): ").strip()
    gpa = input("GPA (like 8.5): ").strip()
    contact = input("Contact (email/phone): ").strip()

    try:
        p = Pupil(sid, full_name, department, int(year), float(gpa), contact)
    except Exception as e:
        print("Invalid input: ", e)
        return

    append_pupil(p)
    print("Record created.")

def show_all_records():
    pupils = load_all()
    if not pupils:
        print("No records found.")
        return
    print("\n--- PUPILS ---")
    for p in pupils:
        print(p.sid, "|", p.full_name, "|", p.department, "| Year:", p.year, "| GPA:", p.gpa)
