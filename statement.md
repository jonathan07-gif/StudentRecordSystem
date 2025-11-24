# app.py
from core.io_module import create_record_interactive, show_all_records
from core.query_module import find_by_name, find_by_department, top_by_gpa
from core.stats_module import count_by_department, avg_gpa_by_department

def menu():
    print("\nStudentRecordSystem - Menu")
    print("1. Create record")
    print("2. View all records")
    print("3. Search by name")
    print("4. List by department")
    print("5. Top students by GPA")
    print("6. Department counts")
    print("7. Department average GPA")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("Choice: ").strip()
        if choice == "1":
            create_record_interactive()
        elif choice == "2":
            show_all_records()
        elif choice == "3":
            q = input("Enter name or part: ").strip()
            res = find_by_name(q)
            if res:
                for p in res:
                    print(p.sid, p.full_name, p.department, p.gpa)
            else:
                print("No match.")
        elif choice == "4":
            d = input("Department: ").strip()
            res = find_by_department(d)
            if res:
                for p in res:
                    print(p.sid, p.full_name, p.year, p.gpa)
            else:
                print("No students in this department.")
        elif choice == "5":
            n = input("How many top students?: ").strip()
            if n.isdigit():
                for p in top_by_gpa(int(n)):
                    print(p.sid, p.full_name, p.gpa)
            else:
                print("Enter a number.")
        elif choice == "6":
            counts = count_by_department()
            for dept, cnt in counts.items():
                print(dept, ":", cnt)
        elif choice == "7":
            avgs = avg_gpa_by_department()
            for dept, avg in avgs.items():
                print(dept, ":", round(avg, 2))
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
