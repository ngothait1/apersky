from person import Person

class Employee(Person):
    def __init__(self, name, age, id_number, field_of_work, salary):
        super().__init__(name, age, id_number)
        self.field_of_work = field_of_work
        self.salary = salary

    def getFieldOfWork(self):
        return self.field_of_work
    
    def getSalary(self):
        return self.salary
    
    def printEmployee(self):
        print(self.getPersonString() + ", The field is " + self.getFieldOfWork() + ", the salary is " + str(self.getSalary()))

    def printMyself(self):
        self.printEmployee()  

    def getType(self):
        return "Employee"