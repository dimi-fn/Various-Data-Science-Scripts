class Identity:
    '''
    Creating a class named "Identity"
    Properties: first name, last name, age
    Method: a function printing the output based on attributes given
    '''

    # assigning values to the object properties of the class "Identity"
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name= last_name
        self.age = age

    # Creating a method (function) belonging to the objects of the "Identity" class:
    def output_function(self):
        print("First Name: {} \nLast Name: {} \nAge: {}".format(self.first_name, self.last_name, self.age))

x = Identity("Peter", "Dosh", 41)
x.output_function()