def tri(size, symb):
    for i in range(size // 2):
        print(symb * (i + 1))
    if size % 2 != 0:
        print(symb * (size // 2 + 1))
    for i in range(size // 2 - 1, -1, -1):
        print(symb * (i + 1))

inp = input().split()
tri(int(inp[0]), inp[1])
