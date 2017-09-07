n = int(input("Enter a number : "))

while n >= -1:

    if n == -1:
        break

    Factorial = 1

    for i in range(1, n+1):
        if n == 0:
            break
        else:
            Factorial = Factorial * i
    
    print("%d! : "%n, Factorial)

    n = int(input("Enter a number : "))

    continue

