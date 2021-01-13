class Student:
    #Initially define studentName as variable
    studentName = ""
    fellowStudents = []

    #Initialise Class
    def __init__(self, name):
        self.studentName = name
    
    #Update name of student in case of error
    def updateName(self, name):
        self.studentName = name
    
    #Return name of student
    def getName(self):
        return self.studentName

    #Add fellow students to list
    def addFellowStudents(self, fellowStudentName):
        self.fellowStudents.append(fellowStudentName)

    #Remove fellow students from list
    def removeFellowStudents(self, fellowStudentName):
        self.fellowStudents.remove(fellowStudentName)

    #Read Fellow students from list - Use this for terminal display
    def readFellowStudents(self):
        x = 1
        for stud in self.fellowStudents:
            print(x, '. ', stud)
            x = x + 1
    
    #Return fellow student list
    def getFellowStudents(self):
        return self.fellowStudents