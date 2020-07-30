from ummu_contacts import find
from ummu_contacts import add
from ummu_contacts import delete
print("*"*47)
print("****Welcome to the my phonebook application****")
print("*"*47)
def myProgram():
    print('1.Find a phone number')
    print("2.Insert a phone number")
    print("3.Delete a person from the phonebook")
    print("4.Terminate")
    option = input ("Select operation from phonebook 1/2/3/4: ")
    if not option.isnumeric() or (not int(option) in [1,2,3,4]):
         print("*"*15)
         print("Please enter a integer in (1/2/3/4: ")
         print("*"*15)
         myProgram()
    else:
        option=int(option)
    if option == 1:
        name = input("Write the person name whose finding: ")
    elif option == 2:
        name = input("Insert name of the person: ")
        number = input("Insert phone numeber of the person: ")
        print(add(name,number))
    elif option ==3:
        name = input("Whom to delete from phonebook: ") 
        print(delete(name))
    elif option == 4:
        exit()
while True:
    myProgram()        




