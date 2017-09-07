def Factorial(inNumber):
    result = 1
    for x in range(2, inNumber+1):
        result *= x
    return result

num = int(input(" Enter a number: " ))
print( "%d!" %num, " = ", "%d" %Factorial(num) )