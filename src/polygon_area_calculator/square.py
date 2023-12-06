from polygon_area_calculator.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, x):
        self.width = x
        self.height = x
        
    def set_side(self, x):
        self.width = x
        self.height = x
        
    def __str__(self):
        return f"Square(side={self.width})"