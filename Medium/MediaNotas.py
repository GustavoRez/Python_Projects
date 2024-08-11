n1 = float(input("Insert your first grade: "))
n2 = float(input("Insert your second grade: "))
n3 = float(input("Insert your third grade: "))

grade = round((n1 + n2 + n3) / 3, 2)
status = (n1 + n2 + n3) / 3 < 6

if(status):
    print("Better study next time. Your average was: ", grade)

else:
    print("Congratulations. Your average was: ", grade)