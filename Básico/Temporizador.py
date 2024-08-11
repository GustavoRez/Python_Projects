import time

num = int(input("Insert a number: "))

for i in range (num, 0, -1):
    print("You have", i, "seconds to defuse the bomb!")
    time.sleep(1)
else:
    print("BOOOOM")
    time.sleep(2)
    print("Oh, looks like it exploded...")