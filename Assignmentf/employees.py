def write_employee_details(filename, employees):
   
    with open(filename, 'w') as file:
        for employee in employees:
            file.write(f"Name: {employee['name']}, Age: {employee['age']}, Salary: {employee['salary']}\n")

def main():
    # List of employee details
    employees = [
        {"name": "John Doe", "age": 30, "salary": 50000},
        {"name": "Jane Smith", "age": 25, "salary": 60000},
        {"name": "Alice Johnson", "age": 28, "salary": 55000},
        {"name": "Bob Brown", "age": 35, "salary": 70000}
    ]

    # File name
    filename = "employees.txt"

    # Write employee details to the file
    write_employee_details(filename, employees)
    print(f"Employee details written to {filename}")

if __name__ == "__main__":
    main()
