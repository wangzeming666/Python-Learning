class Shape():
    def __init__(self):
        pass
    
    def draw(self):
        print(self.x)
        print(self.y)
        if self.x1:
                print(x1)
        if self.x2:
                print(x2)
        if self.r:
                print(r)

    def move(self, x, y):
        self.x += x
        self.y += y

class Point(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle(Shape):
    def __init__(self, x, y, z, q):
        self.x = x
        self.y = y
        self.width = z
        self.high = q

class Line(Shape):
    def __init__(self, x, y, x1, y1):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1

    def move(self, x, y):
        self.x += x
        self.y += y
        self.x1 += x
        self.y1 += y

class Circle(Shape):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

p = Point(float(input()))
r = Rectangle(float(input()))
l = Line(float(input()))
c = Circle(float(input()))
movesize = input()
List = [p, r, l, c]
for i in List:
        i.move(movesize)
        i.draw()
