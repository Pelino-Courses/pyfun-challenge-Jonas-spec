import math

class shape:
    def __init__(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Shape name must be a non_empty string.")
        self.name = name
        def area(self):
            raise NotImplementedError("subclasses must implement this method")
        def __str__(self):
            return f"{self.name} with area: {self.area():.2f}"
        
        class circle(shape):
            def __init__(self, radius: float):
                super().__init__("circle")
                if not isinstance(radius, (int, float)) or radius <= 0:
                    raise ValueError("Radius must be a positive number")
                self.radius = radius
                def area(self):
                    return math.pi * self.radius ** 2
                
                def __str__(self):
                    return f"Circle (radius={self.radius}) with area: {self.area():.2f}"
                
                class rectangle(shape):
                    def __init__(self, width: float, height: float):
                        super().__init__("rectangle")
                        if not all(isinstance(x, (int, float)) and x > 0 for x in (width, height)):
                            raise ValueError("Width and height must be positive numbers")
                        self.width = width
                        self.height = height
                        def area(self):
                            return self.width * self.height
                        def __str__(self):
                            return f"rectangle (width={self.width},height={self.height}) with area: {self.area():.2f}"
                        class triangle(shape):
                            def __init__(self, base: float, height: float):
                                super().__init__("triangle")
                                if not all(isinstance(x, {int, float}) and x > 0 for x in (base, height)):
                                    raise ValueError("Base and Height must be positive numbers")
                                self.base = base
                                self.height = height
                                def area(self):
                                    return 0.5 * self.base * self.height
                                
                                def __str__(self):
                                    return f"triangle (base={self.base}, height={self.height}) with area: {self.area():.2f}"
                                
                                #Example usage
                                if __name__ == "__main__":
                                    shapes = [
                                        circle(5),
                                        rectangle(4,6),
                                        triangle(3,7)
                                    ]
                                    for shape in shapes:
                                        print(shape)
                             