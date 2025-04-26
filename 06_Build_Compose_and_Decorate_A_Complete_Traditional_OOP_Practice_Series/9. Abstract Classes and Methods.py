from abc import ABC, abstractmethod

class Shape(ABC):  # Inherit from ABC (Abstract Base Class)
    @abstractmethod
    def area(self):
        pass  # No implementation in abstract method

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):  # Must implement the abstract method
        return self.length * self.width


rect = Rectangle(5, 3)
print("Rectangle area:", rect.area())  
