from person import Person

class Employee(Person):
    def __init__(self, name, age, id_number):
        super().__init__(name, age, id_number)
        self.field_of_work = input("Enter the field of work: ")
        self.salary = float(input("Enter the salary: "))

    def getFieldOfWork(self):
        return self.field_of_work
    
    def getSalary(self):
        return self.salary
    
    def printEmployee(self):
        print(self.getPersonString() + ", The field is " + self.getFieldOfWork() + ", the salary is " + str(self.getSalary()))

    def printMyself(self):
        self.printEmployee()  

    def getInfoDict(self):
        return {
            "ID": self.getIdNumber(),
            "Name": self.getName(),
            "Age": self.getAge(),
            "Field of Work": self.field_of_work,
            "Salary": self.salary
        }   
# Tests
if __name__ == "__main__":
    test_name = "test_employee"
    test_age = 18
    test_id = 789
    test_field_of_work = "Engineering"
    test_salary = 75000

    employee = Employee(test_name, test_age, test_id)
    employee.field_of_work = test_field_of_work
    employee.salary = test_salary

    if employee.getName() != test_name:
        print("Error: Name should be " + test_name + " but got " + employee.getName())
    if employee.getAge() != test_age:
        print("Error: Age should be " + str(test_age) + " but got " + str(employee.getAge()))
    if employee.getIdNumber() != test_id:
        print("Error: ID should be " + str(test_id) + " but got " + str(employee.getIdNumber()))
    if employee.getFieldOfWork() != test_field_of_work:
        print("Error: Field of work should be " + test_field_of_work + " but got " + employee.getFieldOfWork())
    if employee.getSalary() != test_salary:
        print("Error: Salary should be " + str(test_salary) + " but got " + str(employee.getSalary()))