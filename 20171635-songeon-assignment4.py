def combination(n, m):
    if m == 0:
        return 1
    if m == 1:
        return n
    if n == m:
        return 1
    return combination(n-1, m) + combination(n-1, m-1)

def factorial(n):
    if n == 0:
        return 1
    sumBuf = 1
    while n > 0:
        sumBuf = sumBuf * n
        n = n -1
    return sumBuf

def combinationF(n, m):
    return (factorial(n) // (factorial(m) * factorial(n-m)))

n, m = 100, 82

print(combinationF(n,m))
print(combination(n, m))

