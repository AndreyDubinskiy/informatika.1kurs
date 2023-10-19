inp = input().split(' ')
a = int(inp[0])
b = int(inp[1])

c = 0
while ((a+c)%b!=0 or (b+c)%a!=0):
	c += 1
print(c)