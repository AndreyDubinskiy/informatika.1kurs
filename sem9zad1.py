s = input()
f = str()
s = s[::-1].replace(')', 'o').replace('(', ')').replace('o', '(')
print(s)
arr = list()
for i in s:
    if i.isdigit():
        f += i
    elif i == ')':
        while len(arr) > 0:
            if arr[-1] == '(':
                arr.pop()
                break
            else:
                f += arr.pop()
        print(arr, f)
    elif len(arr) == 0:
        arr.append(i)
    elif (arr[-1] == '-' or arr[-1] == '+'):
        arr.append(i)
    elif i == '*' or i == '/':
        arr.append(i)
    elif (i == '-' or i == '+') and (arr[-1] == '*' or arr[-1] == '/'):
        while len(arr) > 0:
            if arr[-1] == '(':
                arr.pop()
                break
            f += arr.pop()
        arr.append(i)
    elif (i == '-' or i == '+'):
        arr.append(i)
    else:
        arr.append(i)
print(arr)
while len(arr) > 0:
    f += arr.pop()
print(f[::-1])