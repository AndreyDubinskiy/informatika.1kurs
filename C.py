chipsiki = input().split(' ')
n = int(chipsiki[0])
m = int(chipsiki[1])

def john(n=n, m=m):
	if(n%2==0 or m%2==0):
		return 0
	else:
		return 1 + 4 * john((n-1)/2, (m-1)/2)
print(john())