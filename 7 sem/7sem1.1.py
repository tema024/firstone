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

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other, self.z + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, (int, float)):
            return Vector(self.x - other, self.y - other, self.z - other)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def sc(self, vec):
        return self.x * vec.x + self.y * vec.y + self.z * vec.z

    def __mul__(self, num):
        if isinstance(num, (int, float)):
            return Vector(self.x * num, self.y * num, self.z * num)

    def vecadd(self, vec):
        return Vector((self.x + vec.x), (self.y + vec.y), (self.z + vec.z))

    def vecsol(self, vec):
        return Vector((self.x - vec.x), (self.y - vec.y), (self.z - vec.z))


points = []
result = Vector(0, 0, 0)
n = int(input())
for i in range(n):
    coordinates = input().split(' ')
    x, y, z = map(int, coordinates)
    points.append(Vector(x, y, z))
    result = result + points[i]
print(result.x / n, result.y / n, result.z / n)
