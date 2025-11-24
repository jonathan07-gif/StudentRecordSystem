# core/pupil.py
class Pupil:
    def __init__(self, sid, full_name, department, year, gpa, contact):
        self.sid = sid
        self.full_name = full_name
        self.department = department
        self.year = int(year)
        self.gpa = float(gpa)
        self.contact = contact

    def to_row(self):
        return [self.sid, self.full_name, self.department, str(self.year), f"{self.gpa}", self.contact]

    def __repr__(self):
        return f"Pupil({self.sid}, {self.full_name}, {self.department}, {self.year}, {self.gpa}, {self.contact})"
