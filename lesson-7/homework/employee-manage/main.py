import manage as m
import uuid
def main():
    while True:
        print("""
        1. Add new emplyee record
        2. View all employee records
        3. Search for an employee by Employee ID
        4. Update an employee`s information
        5. Delete an employee record
        6. Exit
        """)
        choice = int(input())

        match (choice):
            case 1:
                name = input("enter name of employee")
                position = input("enter position of employee")
                salary = input("enter salary of employee")
                employee = m.employee(uuid.uuid4(),name,position,salary)
                employee.create()
            case 2:
                emp= m.employee()
                employees = emp.get_all()
                for employee in employees:
                    print(f"ID:{employee[0]}\nName:{employee[1]}\nPosition:{employee[2]}\nSalary:{employee[3]}")
                print("\n")
            case 3:
                id = input("enter id of employee")
                emp= m.employee(id)
                emp.get_by_id()
            case 4:
                id = input("enter id of employee")
                name = input("enter name of employee")
                position = input("enter position of employee")
                salary = input("enter salary of employee")
                emp= m.employee(id,name,position,salary)
                emp.update_by_id()
            case 5:
                id = input("enter id of employee")
                emp= m.employee(id)
                emp.delete_by_id()
            case 6:
                break

if __name__ == '__main__':
    main()