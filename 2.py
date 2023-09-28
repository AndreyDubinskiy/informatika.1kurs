def simple(num):
    fac = 2
    res = ''
    while fac ** 2 <= n:
        while num % fac == 0:
            res += str(fac) + '*'
            num //= fac
        fac += 1
    if num > 1:
        res += str(num)
    if res[-1] == '*':
        return res[:-1]
    else:
        return res


n = int(input())
print(simple(n))
