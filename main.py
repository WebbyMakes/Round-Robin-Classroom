from Classroom_Class import Classroom
from Student_Class import Student

print("Please enter date of class")
userinput = input()
myClass = Classroom(userinput)

menu = []
menu.append("1. Add Student")
menu.append("2. Delete Student")
menu.append("3. Update Student")
menu.append("4. Reset Classroom")
menu.append("5. Crunch Numbers")
menu.append("6. Save")
menu.append("7. Load")
menu.append("8. Exit")

runProgram = True
while runProgram == True:
    print("Class size: ", len(Classroom.classList))
    for options in range(len(menu)):
        print(menu[options])
        
    selection = input("Please Select a Menu item using keypad")
    def one():
        myClass.addStudent()
        print("Function one not yet implemented")
    def two():
        print("function two not yet implemented")
    def three():
        print("function three not yet implemented")
    def four():
        print("function four not yet implemented")
    def five():
        print("function five not yet implemented")
    def six():
        print("function six not yet implemented")
    def seven():
        print("function seven not yet implemented")
    def eight():
        print("function eight not yet implemented")

    if selection == 1: one
    elif selection == 2: two
    elif selection == 3: three
    elif selection == 4: four
    elif selection == 5: five
    elif selection == 6: six
    elif selection == 7: seven
    elif selection == 8: eight


print("End of Program")