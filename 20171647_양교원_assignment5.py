import time
import random

def iterfibo(n):
    if (n <= 1):
        return n

    before = [1, 1]
    current = 0
    for count in range(n-2):
        current = before[0] + before[1]
        before[0] = before[1]
        before[1] = current

    return current

def fibo(n):
    if (n <= 1):
        return n

    return fibo(n-1) + fibo(n-2)

while True:
	nbr = int(input("Enter a number: "))
	if nbr == -1:
		break
	ts = time.time()
	fibonumber = fibo(nbr)
	ts = time.time() - ts
	print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))

	ts = time.time()
	fibonumber = iterfibo(nbr)
	ts = time.time() - ts
	print("Iteration Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
