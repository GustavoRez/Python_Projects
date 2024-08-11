key = ["c", "o", "m", "p", "u", "t", "e", "r"]
userWord = ["_"]*len(key)
chances = 0
attempts = [0] * 26

while (userWord != key):
    if (chances >= 7):
        print("You lose :(")
        break

    for letra in userWord:
        print(letra, end='')

    print()
    print()

    if(chances != 0):
        print("You have", 7 - chances, "more attempts.", end=' ')
    inp = input("Insert a letter! ")

    for i in range (0, len(attempts)):
        if(inp == attempts[i]):
            print("This letter has already been computed!")
            print()
            chances -= 1
            break
        else:
            attempts.append(inp)
    

    for i in range(0, len(key)):
        if(inp == key[i]):
            userWord[i] = key[i]
            chances -= 1
                    
    chances += 1

if (chances < 6):
    print("Congraulations! The word was ", *userWord, "!", sep = '')