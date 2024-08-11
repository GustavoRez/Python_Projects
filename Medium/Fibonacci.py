def fibo(x):
    x1 = 1
    x2 = 1
    x3 = 0
    for i in range(0, x):
        print(x1)
        x3 = x1 + x2   
        x1 = x2             
        x2 = x3    

print("Fibonacci sequence")
fibo(int(input("Insert a number: ")))