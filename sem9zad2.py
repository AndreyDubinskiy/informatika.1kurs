s = input()
s1 = ''
arr = list()
c = 0
for i in range(len(s)):
    if s[i] == ' ' and s1 != '':
        arr.append(s1)
        s1 = ''
    elif s[i].isdigit():
        s1 += s[i]
    elif s[i] == '+':
        arr.append(int(arr.pop()) + int(arr.pop()))
    elif s[i] == '-':
        arr.append(-int(arr.pop()) + int(arr.pop()))
    elif s[i] == '*':
        arr.append(int(arr.pop()) * int(arr.pop()))
    elif s[i] == '/':
        arr.append((1 / int(arr.pop())) * int(arr.pop()))
    else:
        pass
if len(arr) == 1:
    print(arr)
else:
    print('Некорректно')
