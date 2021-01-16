class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, point):
        return (point.x - self.x, point.y - self.y)

p = Point(3, 5)
print(p.x)
print(p.y)

print(p.calculate_distance(Point(4, 7)))