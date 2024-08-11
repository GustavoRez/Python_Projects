NumLeft = int(input("Insert the numbering: "))
NumRight = int(input("Insert the numerator: "))

for i in range(1, NumRight + 1):
    print(NumLeft, "*", i, "=", NumLeft * i)
else:
    print ("This was the table of", NumLeft, "multipling to", NumRight)
