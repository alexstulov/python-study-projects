class Rectangle:
    width = 0
    height = 0
    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height
        
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        if (self.width > 50 or self.height > 50):
            return "Too big for picture."
        y = 0
        result = ''
        while y < self.height:
            result += '*' * self.width + '\n'
            y += 1
        return result
                
    def get_amount_inside(self, shape):
        horizontal_amount = int(self.width / shape.width)
        vertical_amount = int(self.height / shape.height)
        return horizontal_amount * vertical_amount
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"