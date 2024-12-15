class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def prefix_sum(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

    def range_sum(self, left, right):
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index


A=[1,2,3,4,5,6,7]

fen = FenwickTree(len(A))
for i, value in enumerate(A):
    fen.update(i + 1, value)

print(fen.prefix_sum(6))
print(fen.range_sum(3,5))
fen.update(3, 10 - 3)  #Заменим А[3] = 10
print(fen.range_sum(2, 5))
