A=list(map(int,input().split()))
g=A[0]
A.pop(0)
z=1
for i in range (len(A)):
    z=z*A[i]
m=1
for i in range (1,g+1):
    m=m*i
print(int(m/z))
