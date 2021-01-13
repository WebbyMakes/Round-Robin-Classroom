import math
from random import randint

class Group:
    #Initial Parameters
    minGroupSize = 3
    maxGroupSize = 5
    optimalGroupSize = 4

    studentNum = 0
    
    numberOfOpGroups = 0 #Defines how many groups with a groups size of 'optimalGroupSize'
    remainderGroupSize = 0 #Defined how many people will fit into the remainder group
    
    sizeOfGroupArr = []

    roundOneNumbers = []
    roundTwoNumbers = []
    roundThreeNumbers = []

    def __init__(self):
        print("Group Created")

    def initialiseGroups(self, numberOfStudents):
        self.studentNum = numberOfStudents
        self.numberOfOpGroups = math.floor(numberOfStudents / self.optimalGroupSize)
        self.remainderGroupSize = self.studentNum % self.optimalGroupSize

        if self.numberOfOpGroups < 1:
            self.sizeOfGroupArr.append(self.studentNum)
        elif self.numberOfOpGroups >= 1:
            for count in range(1, self.numberOfOpGroups):
                self.sizeOfGroupArr.append(4)
            if self.remainderGroupSize == 0:
                self.sizeOfGroupArr.append(4)
            elif self.remainderGroupSize == 1:
                self.sizeOfGroupArr.append(5)
            elif self.remainderGroupSize == 2:
                self.sizeOfGroupArr.append(3)
                self.sizeOfGroupArr.append(3)
            elif self.remainderGroupSize == 3:
                self.sizeOfGroupArr.append(4)
                self.sizeOfGroupArr.append(3)
            
    def returnGroupSize(self):
        print("Size of Groups: ", self.sizeOfGroupArr)

    def printGroupInfo(self):
        print("Number of optimal groups: ", self.numberOfOpGroups)
        print("Students Remainder: ", self.remainderGroupSize)

    def sortGroup(self):
        numberOfGroups = len(self.sizeOfGroupArr)
        for count in range(0, self.studentNum):
            num = randint(0, numberOfGroups)
            


#Test Casing
#system('clear')
myGroup = Group()
myGroup.initialiseGroups(17)
myGroup.printGroupInfo()
myGroup.returnGroupSize()