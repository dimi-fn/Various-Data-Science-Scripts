# comment

'''
multi-line comment
'''

# variable declaration
x = 10


# naming a variable
first_name = "Alex"

# constants
TAX_RATE = 22

# print
print(x, first_name)

print("x = {} and first name is: {}".format(x, first_name))

print("Type of x is: {}".format(type(x)))

# floor division
print(10//3)

# classes and methods
class Car:
    def __init__(self, brand, colour):
        self.brand = brand
        self.colour = colour

    # function method
    def print_output(self):
        print ("Brand of car is {} and the colour is {}".format(self.brand, self.colour))

result= Car(brand="mercedes", colour="black")
result.print_output()