from person import Person

class Student(Person):
    def __init__(self, name, age, id_number, field_of_study, year_of_study, score_avg):
        super().__init__(name, age, id_number)
        self.field_of_study = field_of_study
        self.year_of_study = year_of_study
        self.score_avg = score_avg

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
    
    def getType(self):
        return "Student"
