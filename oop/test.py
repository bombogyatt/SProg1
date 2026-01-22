class Point:

    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

class Rectangle:

    def __init__(self, point1, point2, point3, point4):
        self.p1 = point1
        self.p2 = point2
        self.p3 = point3
        self.p4 = point4

    def move(self, dx, dy):
        self.p1.x += dx
        self.p2.x += dx
        self.p3.x += dx
        self.p4.x += dx
        
        self.p1.y += dy
        self.p2.y += dy
        self.p3.y += dy
        self.p4.y += dy

    def area(self):
        a = abs(self.p1.x - self.p2.x)
        b = abs(self.p2.y - self.p3.y)

        return a*b



p = Point(2, 3)
print(p.x, p.y)

r = Rectangle(
    Point(1, 2),
    Point(5, 2),
    Point(5, 6),
    Point(1, 6)
)
print(r.p1.x, r.p1.y)
print(r.p3.x, r.p3.y)


r.move(2, -1)
print(r.p1.x, r.p1.y)
print(r.p4.x, r.p4.y)


print(r.area())