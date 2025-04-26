def add_greeting(cls):
    # Add a new method to the class
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls  # Return the modified class

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name


p = Person("Mehtab")
print(p.greet()) 
print(p.name)    