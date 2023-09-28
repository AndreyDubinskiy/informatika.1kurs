def alg(num1, num2):
    if num1 == 0:
        return (0, 1, num2)
    else:
        x, y, d = alg(num2 % num1, num1)
    return (y - (num2 // num1) * x, x, d)

a, b = input().split()
print(*alg(int(a), int(b)))
