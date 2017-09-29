import time

def iterfibo(n):
    A = 0
    B = 1
    C = 0
    for i in range(2, n+1):
        C = A + B
        A, B = B, C
    return C

def fibo(n):
    return n if n <= 1 else fibo(n-1) + fibo(n-2)

while True:
    nbr = int(input("Enter a number : "))
    if nbr == -1:
        break
    if nbr < 0:
        print("음수는 출력할 수 없습니다")
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() -ts
    print("IterFibo(%d) = %d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() -ts
    print("Fibo(%d) = %d, time %.6f" %(nbr, fibonumber, ts))
    
