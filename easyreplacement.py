import random
class Monoalphabet:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, keytable, keytable1):
        lowercase_code = {x: y for x, y in zip(self.alphabet, keytable)}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, keytable)}
        self._encode = lowercase_code
        self._encode.update(uppercase_code)
        lowercase_code = {x: y for x, y in zip(self.alphabet, keytable1)}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, keytable1)}
        self._decode = lowercase_code
        self._decode.update(uppercase_code)

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, text):
        return ''.join([self._decode.get(char, char) for char in text])


def ch(line):
    arr = {}
    for i in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
        arr.update({i: 0})
        arr[i] += line.count(i)
    for i in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
        arr[i] = (arr[i] / len(line)) * 100
    print(sorted(arr.items(), key=lambda x: x[1]))


key = "птхиёшцрыязэчджвфгму_юьоксещйбанл"
key1 = 'эьормщднйгычясюцажшбтпвёле__зхкфи'
cipher = Monoalphabet(list(key), list(key1))
line = input()
ch(line)
while line != '!!!':
    print(cipher.encode(line))
    print(cipher.decode(line))
    line = input()
    ch(line)
