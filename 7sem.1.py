class Vector:
    def __init__(self, x, y, z):
        assert isinstance(x, (int, float))
        assert isinstance(y, (int, float))
        assert isinstance(z, (int, float))
        self.x = x
        self.y = y
        self.z = z

    def vec(self):
        return self.x, self.y, self.z

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __add__(self, num):
        return Vector(self.x + num, self.y + num, self.z + num)

    def __radd__(self, num):
        return 'false'

    def __sub__(self, num):
        return Vector(self.x - num, self.y - num, self.z - num)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def sc(self, vec):
        return self.x * vec.x + self.y * vec.y + self.z * vec.z

    def __mul__(self, num):
        return Vector(self.x * num, self.y * num, self.z * num)

    def vecadd(self, vec):
        return Vector((self.x + vec.x), (self.y + vec.y), (self.z + vec.z))

    def vecsol(self, vec):
        return Vector((self.x - vec.x), (self.y - vec.y), (self.z - vec.z))

a = Vector(1, 2, 3)
b = Vector(4, 5, 6)
num = 3

print('Vector a:', a.vec())
print('Vector b:', b.vec())
print('Vector a + num:', a + num)
print('num + Vector a:', num + a)
print('Vector a * num:', a * num)
print('Vector a - num:', a - num)
print('module Vector a:', abs(a))
print('scalar product Vector a * Vector b:', a.sc(b))
print('Vector a + Vector b:', a.vecadd(b).vec())
print('Vector a - Vector b:', a.vecsol(b).vec())
