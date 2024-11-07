class Person:
    def __init__(self, name, age, id_number):
        self._name = name    
        self._age = age       
        self._id_number = id_number

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def getIdNumber(self):
        return self._id_number

    def getPersonString(self):
        return "The person " + self.getName() + " ID: " + str(self.getIdNumber()) + " is " + str(self.getAge()) + " years old"

    def printMyself(self):
        print(self.getPersonString())

    def getType(self):
        return "Person"
# Tests
if __name__ == "__main__":
    test_name = "test_name"
    test_age = 80
    test_id = 123
    person = Person(test_name, test_age, test_id)
    if person.getAge() != test_age:
        print("Error: Age should be " + str(test_age) + " but i got " + str(person.getAge()))
    if person.getName() != test_name:
        print("Error: name should be " + test_name + " but i got " + person.getName())
    if person.getIdNumber() != test_id:
        print("Error: ID should be " + test_id + " but i got " + person.getIdNumber())
    
