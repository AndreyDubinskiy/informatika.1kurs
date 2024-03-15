import numpy as np


class SegmentTree:
    def __init__(self, data, func=lambda a, b: a + b, neutral_elements=0):
        self.data = data
        self._func = func
        self.neutral_elements = neutral_elements
        self.build_tree()

    def build_tree(self) -> None:
        ln = len(self.data)
        lb = np.log2(ln)
        if lb == int(lb):
            self.data = self.data
            self.neutral_elements = 0
        else:
            self.data = self.data
            lb = int(lb) + 1
            self.neutral_elements = 2 ** lb - ln
            for i in range(ln, 2 ** lb):
                self.data.append(0)
        self.tree = [0 for i in range(len(self.data) - 1)] + self.data
        self._size = len(self.data)
        self.calc_tree()

    def calc_tree(self) -> None:
        for i in range(len(self.tree) + 1, 2, -2):
            s1 = self.tree[i - 2]
            s2 = self.tree[i - 3]
            sm = s1 + s2
            self.tree[(i - 4) // 2] = sm

    def query(self, start, stop):
        self.tree.insert(0, 36)
        start += self._size
        stop += self._size
        if start == stop:
            return self.tree[stop]
        else:
            stop += 1
            res_left = res_right = 0
            while start < stop:
                if start % 2 == 1:
                    res_left = self._func(res_left, self.tree[start])
                    start += 1
                if stop % 2 == 1:
                    stop -= 1
                    res_right = self._func(self.tree[stop], res_right)
                start = start // 2
                stop = stop // 2
            self.tree.pop(0)
            return self._func(res_left, res_right)

    def __getitem__(self, idx):
        return self.data[idx]

    def update(self, left_border, right_border, value):
        if int(self.neutral_elements) == 0:
            for i in range(left_border, right_border + 1):
                self.data[i] += value
            self.build_tree()
        else:
            del self.data[-(int(self.neutral_elements)):]
            for i in range(left_border, right_border + 1):
                self.data[i] += value
            self.build_tree()


tree = SegmentTree([1, 2, 3, 4, 5, 6, 7, 8])
print(tree.data)

print(tree.query(0, 7))

print(tree.tree)
print(tree.data)

tree.update(2, 4, 5)

print(tree.data)
print(tree.tree)
