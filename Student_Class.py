class Student:
    #Initially define studentName as variable
    studentName = ""

    #Initialise Class
    def __init__(self, name):
        self.studentName = name
    #Update name of student in case of error
    def updateName(self, name):
        self.studentName = name
    #Return name of student
    def getName(self):
        return self.studentName