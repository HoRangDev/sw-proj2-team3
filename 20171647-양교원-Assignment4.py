def Factorial(n):
    result = 1
    if (n!=0):
        for i in range(2, n+1):
            result *= i
    return result

def RecursivelyFacto(n):
    if ( n <= 1 ):
        return 1
    return n * RecursivelyFacto(n-1)

def Combination(n, m):
    answer = (Factorial(n)/(Factorial(m) * Factorial(n-m)))
    return answer

def RecursivelyCombi(n, m):
    if ( n < m ):
        return 0
    if ( n == m ) or (m == 0):
        return 1
    return RecursivelyCombi(n-1,m) + RecursivelyCombi(n-1, m-1)


print(RecursivelyFacto(4))
print(Combination(6, 3))
print(RecursivelyCombi(6,3))
