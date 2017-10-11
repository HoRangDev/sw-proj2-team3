import time

def iterfibo(n):
    if (n <= 1):
        return n

    before = [1, 1]
    current = 1
    for count in range(n-2):
        current = before[0] + before[1]
        before[0] = before[1]
        before[1] = current

    return current

def fibo(n, count):
    count[0] += 1
    if (n <= 1):
        return n

    return fibo(n-1, count) + fibo(n-2, count)

while True:
	nbr = int(input("Enter a number: "))
	if nbr == -1:
		break
	ts = time.time()
	count = [0]
	fibonumber = fibo(nbr,count)
	ts = time.time() - ts
	print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
	print("Function recursively called: " + str(count[0]) + " times!")

	ts = time.time()
	fibonumber = iterfibo(nbr)
	ts = time.time() - ts
	print("Iteration Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
