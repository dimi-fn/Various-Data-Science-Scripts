class my_class:
  x = 3

p1 = my_class()
print(p1.x)

class Person:
    def __init__(self, name, age):

        # assigning values to object properties:
        self.name = name
        self.age = age

p1 = Person("Peter", 41)
print("Name: {}, Age: {}".format(p1.name, p1.age))