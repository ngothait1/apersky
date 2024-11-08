from person import Person

class Student(Person):
    def __init__(self, name, age, id_number):
        super().__init__(name, age, id_number)
        self.field_of_study = input("Enter the field of study: ")
        self.year_of_study = int(input("Enter the year of study: "))
        self.score_avg = float(input("Enter the average score: "))

    def getFieldOfStudy(self):
        return self.field_of_study
    
    def getYearOfStudy(self):
        return self.year_of_study
    
    def getScoreAvg(self):
        return self.score_avg
    
    def printStudent(self):
        print(self.getPersonString() + ", The field of study is " + self.getFieldOfStudy() + " , the year of study is " + str(self.getYearOfStudy()) + ", the avg is " + str(self.getScoreAvg()))

    def printMyself(self):
        self.printStudent()  
    
    def getInfoDict(self):
        return {
            "ID": self.getIdNumber(),
            "Name": self.getName(),
            "Age": self.getAge(),
            "Field of Study": self.field_of_study,
            "Year of Study": self.year_of_study,
            "Average Score": self.score_avg
        }
# Tests
if __name__ == "__main__":
    test_name = "test_student"
    test_age = 17
    test_id = 456
    test_field_of_study = "Computer Science"
    test_year_of_study = 2
    test_score_avg = 85.5

    student = Student(test_name, test_age, test_id)
    student.field_of_study = test_field_of_study
    student.year_of_study = test_year_of_study
    student.score_avg = test_score_avg

    if student.getName() != test_name:
        print("Error: Name should be " + test_name + " but got " + student.getName())
    if student.getAge() != test_age:
        print("Error: Age should be " + str(test_age) + " but got " + str(student.getAge()))
    if student.getIdNumber() != test_id:
        print("Error: ID should be " + str(test_id) + " but got " + str(student.getIdNumber()))
    if student.getFieldOfStudy() != test_field_of_study:
        print("Error: Field of study should be " + test_field_of_study + " but got " + student.getFieldOfStudy())
    if student.getYearOfStudy() != test_year_of_study:
        print("Error: Year of study should be " + str(test_year_of_study) + " but got " + str(student.getYearOfStudy()))
    if student.getScoreAvg() != test_score_avg:
        print("Error: Average score should be " + str(test_score_avg) + " but got " + str(student.getScoreAvg()))