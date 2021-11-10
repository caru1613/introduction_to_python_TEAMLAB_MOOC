class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def about_me(self):
        print("My name is ", self.name, "My age is ", str(self.age))

class Employee(Person):
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name, age, gender)
        self.salary = salary
        self.hire_date = hire_date
    def do_work(self):
        print("It works hard")
    def about_me(self):
        super().about_me()
        print("My Salary is", self.salary, "My hired date is", self.hire_date)

first_employee = Employee("BY", 39, "Man", 100, 19820621)
first_employee.about_me()
first_employee.do_work()