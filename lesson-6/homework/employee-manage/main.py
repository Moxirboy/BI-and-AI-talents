import manage as m

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
                m.create(name,position,salary)
            case 2:
                employees = m.get_all()
                for employee in employees:
                    print(f"ID:{employee[0]}\nName:{employee[1]}\nPosition:{employee[2]}\nSalary:{employee[3]}")
                print("\n")
            case 3:
                id = input("enter id of employee")
                m.get_by_id(id)
            case 4:
                id = input("enter id of employee")
                name = input("enter name of employee")
                position = input("enter position of employee")
                salary = input("enter salary of employee")
                m.update_by_id(id,name,position,salary)
            case 5:
                id = input("enter id of employee")
                m.delete_by_id(id)
            case 6:
                break

if __name__ == '__main__':
    main()