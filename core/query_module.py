# core/query_module.py
from core.db import load_all

def find_by_name(part):
    part = part.lower()
    return [p for p in load_all() if part in p.full_name.lower()]

def find_by_department(dept):
    dept = dept.lower()
    return [p for p in load_all() if p.department.lower() == dept]

def top_by_gpa(n=5):
    pupils = load_all()
    return sorted(pupils, key=lambda x: x.gpa, reverse=True)[:n]
