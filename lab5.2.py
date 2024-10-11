class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius
        return self.radius

circle = Circle(50)
print(circle.get_radius())
print(circle.set_radius(100))
