import os

def add(x):
    list.append(x)
    print("Item added. Full list:")
    for i in range (0, len(list)):
        print(list[i])

def rem(x):
    for item in list:
        if (item == x):
            list.remove(item)        
    print("Item removed. Full list: ")
    for i in range (0, len(list)):
        print(list[i])


list = ["Banana", "Apple"]
quit = 1
clear = lambda: os.system('cls')

while (quit == 1):
    inp = input("What do you want to do? ")
    
    if(inp == "Show"):
        for i in range (0, len(list)):
            print(list[i])

    elif(inp == "Add"):
        add(input("What item do you want to add? "))

    elif(inp == "Remove"):
        rem(input("What item do you want to remove? "))
    
    elif(inp == "Quit"):
        quit = 0

    elif(inp == "Clear"):
        clear()

    else:
        print("Invalid command! These are my commands: Show, Add, Remove, Clear e Quit.")