def Factorial(inNumber):
    if ( inNumber <=  0 ):
        return 1

    result = 1
    for x in range(2, inNumber+1):
        result *= x
    return result

num = int(input(" Enter a number: " ) )
while ( num != -1 ):
    print( "%d!" %num, " = ", "%d" %Factorial(num) )
    num = int(input(" Enter a number: " ) )
