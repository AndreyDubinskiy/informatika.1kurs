def fib(n):
	if(n == 0):
		return 'a'
	elif(n==1):
		return 'b'
	else:
		return fib(n-2) + fib(n-1)

fib_list = [fib(i) for i in range(31)]
t = int(input())
l = []
for i in range(t):
	l.append(list(map(int, input().split())))
for i in range(t):
	n = l[i][0]
	k = l[i][1] - 1
	print(fib_list[n][k])