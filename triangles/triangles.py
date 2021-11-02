from math import sqrt, acos, isclose


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_cords(self):
        return self.x, self.y


class Vector:
    def __init__(self, a=None, b=None):
        if isinstance(a, Point) and isinstance(b, Point):
            self.x = a.x - b.x
            self.y = a.y - b.y
        elif isinstance(a, int) and isinstance(b, int):
            self.x = a
            self.y = b

    def get_length(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y


def angle(a: Vector, b: Vector):
    return acos(a * b / (a.get_length() * b.get_length()))


class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        self.a = Vector(a=p1, b=p2)
        self.b = Vector(a=p2, b=p3)
        self.c = Vector(a=p3, b=p1)

    def get_angles(self):
        return sorted([angle(self.a, self.b), angle(self.b, self.c), angle(self.c, self.a)])


def alike(t1: Triangle, t2: Triangle):
    angles1 = t1.get_angles()
    angles2 = t2.get_angles()

    for i in range(3):
        if not isclose(angles1[i], angles2[i]):
            return False

    return True


def three_alike(t1: Triangle, t2: Triangle, t3: Triangle):
    return alike(t1, t2) and alike(t2, t3)


def gen_triangles(a, b, d):
    A = Point(a, 0)
    B = Point(b, 0)
    C = Point(0, a)
    D = Point(0, d)
    P = Point(int(a/2), int(a/2))

    return Triangle(D, C, P), Triangle(D, P, B), Triangle(P, A, B)
