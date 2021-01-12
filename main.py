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
        
    selection = input("Please Select a Menu item using keypad \n")
    print("Option ", selection, " selected. \n")
    if selection == "1":
        myClass.addStudent()
        print("Function one not yet implemented")
    elif selection == "2":
        print("Function two not yet implemented")
    elif selection == "3":
        print("Function three not yet implemented")
    elif selection == "4":
        print("Function four not yet implemented")
    elif selection == "5":
        print("Function five not yet implemented")
    elif selection == "6":
        print("Function six not yet implemented")
    elif selection == "7":
        print("function seven not yet implemented")
    elif selection == "8":
        print("Function eight not yet implemented")


print("End of Program")