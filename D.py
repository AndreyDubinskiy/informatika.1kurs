a = input()
l =list(map(int, input().split()))
size = len(l)
m = l[:]

for i in range(size - 2, -1, -1):
	m[i] = max(l[i], m[i + 1])

babki = 0
for i in range(size):
	babki += m[i] - l[i]
print(babki)