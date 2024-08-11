def show():
    for i in range (0, len(num)):
        print(i + 1, "- Name:", name[i], "| Number:", num[i])
        print()

def add(list, x):
    list.append(x)

def rem(nameList, numberList, x, evita):
    try:
        numberList.index(x)
        local = numberList.index(x)

    except ValueError:
        local = "Number not found. No contacts were deleted."

    if (isinstance(local, int)):
        del nameList [local]
        del numberList[local]
        print("Contact deleted! Full list: ")
        show()
    else:
        print(str(local))


name = ["Gustavo Rezende", "João"]
num = ["13123456789", "4"]
quit = 1

while (quit == 1):
    inp = input('What do you want to do? ')
    
    if(inp.lower() == "add"): #Add contacts to list (CREATE)
        newName = input("What is the contact name? ")
        newNumber = input("What is the contact number? ")

        print(newName, newNumber)
        check = input("Is the data correct? ")

        while(check.lower() != "yes"):
            if(check.lower() == "no"):
                nvNome = input("What is the contact name? ")
                nvNum = input("What is the contact number? ")

                print(newName, newNumber)
                check = input("Is the data correct? ")

            else:
                print()
                print("Unrecognized response! Use only yes or no.")
                check = input("Is the data correct? ")

        add(name, newName)
        add(num, newNumber)
        print()
        show()
        print("Contact added!")
        print()

    elif(inp.lower() == "show"): #show contacts from list (READ)
        show()

    elif(inp.lower() == "update"): #Update contact from list (UPDATE)
        contact = input("What contact will be updated? ")

        for i in range(0, len(num)):
            verif = -1
            if(num[i] == contact):
                verif = name[i]
                print(name[i])
                confirm = input("Do you want to update this number? ")
                if(confirm.lower() != "yes"):
                    while(confirm.lower() != "yes"):
                        ctt = input("What contact will be updated? ")
                        for i in range(0, len(num)):
                            if(num[i] == ctt):
                                print(name[i])
                                confirm = input("Do you want to update this number? ")

                elif(confirm.lower() == "yes"):
                    value = num.index(contact)
                    del name[value]
                    del num[value]
        if(verif == -1):
            print()
            print("Name not found. A new contact will be added! Type 'Cancel' to cancel or press 'Enter' to continue.")
        else:
            print("Pressione 'Enter' para continuar.")

        while(input() != "Cancel"):
            newName = input("What is the new contact name? ")
            newNumber = input("What is the new contact number? ")

            print(newName, newNumber)
            print()
            check = input("Is the data correct? ")

            while(check.lower() != "yes"):
                if(check.lower() == "no"):
                    nvNome = input("What is the new contact name? ")
                    nvNum = input("What is the new contact number? ")

                    print(nvNome, nvNum)
                    check = input("Is the data correct? ")

                else:
                    print()
                    print("Unrecognized response! Use only yes or no.")
                    check = input("Is the data correct? ")

            add(name, newName)
            add(num, newNumber)
            print()
            show()
            print("Contact updated!")
            print()
            break

    elif(inp.lower() == "remove"): #Remove contact from list (DELETE)
        rem(name, num, input("What contact will be deleted? "), None)

    elif(inp.lower() == "quit"): #Quit program
        quit = 0

    else: #Program commands
        print("Unrecognized command! My commands are: add, show, update, remove, and quit.")