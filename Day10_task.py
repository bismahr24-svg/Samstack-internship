# Task 1: The Base Class & Single Inheritance

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"


    # Task 2: Method in Base Class
    def work(self):
        print("Employee is performing general duties.")
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    def work(self):
        print(f"{self.name} is writing code in {self.programming_language}.")
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    def work(self):
        print(f"{self.name} is managing a team of {self.team_size} developers.")


# Task 3: Polymorphism in Action
developer = Developer("Fatima", 80000, "Python")
manager = Manager("Ali", 100000, 5)
employees = [developer, manager]
for employee in employees:
    print(employee.get_details())
    employee.work()
