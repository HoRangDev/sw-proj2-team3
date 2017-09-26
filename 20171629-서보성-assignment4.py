def Factorial(n):
    return 1 if n == 1 or n == 0 else Factorial(n-1) * n

def Combination_1(n, m):    
    return 1 if m == 0 or m == n else Combination_1(n-1, m) + Combination_1(n-1, m-1)

while True:
    n = float(input("N = "))
    m = float(input("M = "))
    
    if n/2 < m:
        m = n-m

    if n <= 0 or m < 0 or n < m:
        print("에러 발생")
    else:
        Answer = Factorial(n) / Factorial(m) / Factorial(n-m)
        print("Cf(%d, %d) = %d" %(n, m, Answer))
        print("Cf(%d, %d) = %d" %(n, m, Combination_1(n, m)))

    if n == -1:
        break
