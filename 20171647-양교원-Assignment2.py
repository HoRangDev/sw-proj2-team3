def Factorial(inNumber):
    if ( inNumber ==  0 ):
        return 1

    result = 1
    for x in range(2, inNumber+1):
        result *= x
    return result
#end of Factorial func

def GetNumberInput():
    num = 0
    try:
        num = int(input(" Enter a number: " ) )
    except ValueError:
        print("Wrong input value! <Casting Exception>")
        return -1
    finally:
        return num
#end of GetNumberInput func

#main
num = GetNumberInput()
while ( num != -1 ):
    if ( num == -1 ):
        break
    elif ( num < -1 ):
        print("Wrong value")
    else:
        print( "%d!" %num, " = ", "%d" %Factorial(num) )

    num = GetNumberInput()
#end of while

#end of main
