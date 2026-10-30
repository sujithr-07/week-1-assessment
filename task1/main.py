import csv

#function using *args and **kwargs

def bonus(salary, rate=0.1, *extras, **options):
    result = salary * rate+sum(extras)

    if "cap" in options:
        result = min(result, options["cap"])

    return result

# custom exception

class InvalidSalaryError(Exception):
    pass

# employee class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        if salary < 0:
            raise InvalidSalaryError(f"Invalid Salary:{salary}")
        
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"


# manager inherits from employee class
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return (
            f"Name: {self.name}, Salary: {self.salary},"
            f"team_size: {self.team_size}"
        )

# read emoployee data from csv file
with open("employees.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    employees = list(reader)

#convert employee from string to integer
for employee in employees:
    employee["salary"] = int(employee["salary"])

#list comphrehension:employees with salary above 50000
above_50k = [
    employee["name"]
    for employee in employees
    if employee["salary"] > 50000
]
print("above 50000:", above_50k)

#map and lambda: add 10% raise
salaries=list(map(lambda salary: salary * 1.10, 
                  [employees["salary"] for employees in employees]))
print("salaries after 10% Raise:", salaries)

#filter: keep chennai employees
chennai_employees = list(
    filter(lambda employee: employee["city"] == "Chennai", employees)
)
print("Chennai:", [employee["name"] for employee in chennai_employees])

#test bonus function
print("Bonus:", bonus(50000))
print("Bonus with extras:", bonus(50000, 0.1, 1000, 2000))
print("Bonus with cap:", bonus(50000, 0.1, 1000, cap=4000))

#test employee and manager classes
employee= Employee("Arun", 30000)
print(employee.get_details())
print("Annual Salary:", employee.annual_salary())

manager = Manager("Priya", 60000, 5)
print(manager.get_details())
print("Annual Salary:", manager.annual_salary())

#handle custom exception
try:
    invalid_employee = Employee("test", -500)

except InvalidSalaryError as error:
    print(f"Error: {error}")

finally:
    print("Transaction completed.")

#for loop with continue and break
salaries_to_check = [30000, 0, 45000, 60000, 90000, 68000]

for salary in salaries_to_check:
    if salary == 0:
        continue

    if salary > 85000:
        break

    print(f"Processing salary: {salary}")