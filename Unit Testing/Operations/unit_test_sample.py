def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        raise ValueError("Can not divide by zero")
    return x/y

# non-unit testing 
## bad way
print(add(10,5))