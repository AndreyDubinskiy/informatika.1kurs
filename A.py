num_list = list(map(int, input().split()))
size = len(num_list)
arr = [0]*size
if (size > 0):
	arr[0] = num_list[0]
if (size > 1):
	arr[1] = max(num_list[0], num_list[1])
for i in range(2, size):
	arr[i] = max(num_list[i] + arr[i - 2], arr[i - 1])
print(arr[-1])