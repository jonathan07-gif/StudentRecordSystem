# core/db.py
import csv
import os
from core.pupil import Pupil

CSV_PATH = os.path.join("data", "students.csv")
HEADER = ["student_id","full_name","department","year","gpa","contact"]

def ensure_file():
    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
    if not os.path.exists(CSV_PATH):
        with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(HEADER)

def append_pupil(pupil: Pupil):
    ensure_file()
    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(pupil.to_row())

def load_all():
    ensure_file()
    pupils = []
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            if not r or not r.get("student_id"):
                continue
            p = Pupil(r["student_id"], r["full_name"], r["department"], int(r["year"]), float(r["gpa"]), r["contact"])
            pupils.append(p)
    return pupils

def overwrite_all(pupils):
    ensure_file()
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)
        for p in pupils:
            writer.writerow(p.to_row())
