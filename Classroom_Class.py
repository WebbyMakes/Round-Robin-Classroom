from Student_Class import Student

class Classroom():
    #Define initial Classname for program log (Use date and/or time for this)
    class_Name = ""
    classList = []

    #Initilise Class
    def __init__(self, className):
        self.class_Name = className
    #Create and add student to class list
    def addStudent(self):
        print("Please enter the new students name")
        studentName = input()
        newStudent = Student(studentName)
        self.classList.append(newStudent)
        #Print message is successful
        print("Student Added Successfully")

    def removeStudent(self):
        print("Class List")
        x = 1
        for stud in self.classList:
            print(x, '. ', stud.getName())
            x = x + 1
        print("Please select which student to remove")
        userInput = input()
        del self.classList [int(userInput) - 1]

    def ReadClassList(self):
        print("Classroom")
        for student in self.classList:
            print("- ", student.getName())
        print("\n")
    
    def clearClassroom(self):
        self.classList.clear()
