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

    def ReadClassList(self):
        for student in self.classList:
            print(student.getName())
