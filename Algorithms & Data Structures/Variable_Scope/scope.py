'''
LEGB
* Local > Enclosing > Global > Built-in scope
     * Python will fist look at the local, then at the enclosing, then at the global, and finally at the build-in scope

'''


'''
x = 'global x'
def test():
     y = 'local y'
     print(y)
test() # prints 'local y'    
'''

'''
x = 'global x'
def test():
     y = 'local y'
     # print(y)
     print(x)
test() # prints 'global x'    
print(y) # prints 'NameError: name y is not defined
'''


'''
x = 'global x'
def test():
     y = 'local y'
     # print(y)
     print(x)
test() # prints 'global x'    
print(x) # prints 'global x' 

'''

'''
x = 'global x'
def test():
     x = 'local x'
     # print(y)
     print(x)
test() # prints 'local x' because local scope has priority over the global one   
print(x) # prints 'global x' 
'''

'''
x = 'global x'
def test():
     global x 
     x = 'local x'
     # print(y)
     print(x)
test() # prints 'local x' 
print(x) # prints 'local x' 
'''

'''
# x = 'global x'
def test():
     # global x 
     x = 'local x'
     # print(y)
     print(x)
test() # prints 'local x' 
print(x) # prints 'NameError: name 'x' is not defined' 
'''

'''
# x = 'global x'
def test(z):
     x = 'local x'
     # print(y)
     print(z)
test('local z') # prints 'local z' 
# print(x) # prints '' 
'''

# *************************************** Built-in scope ***************************************

'''
# import builtins
# print(dir(builtins))

m = min([4,10,13,5,2])
print(m)


def test(z):
     x = 'local x'
     # print(y)
     print(z)
test('local z') # prints 'local z' 
'''

# *************************************** Enclosing scope ***************************************

'''
def outer():
     x = 'outer_x' # this is local to the 'outer' function
     def inner():
          x = 'inner_x' # this is local to the 'inner' function
          print(x)
     inner()
     print(x)
outer()  
# prints:
# 'inner_x'
# 'outer_x'
'''


'''
def outer():
     x = 'outer_x' # this is local to the 'outer' function
     def inner(): # enclosing function
          # x = 'inner_x' # this is local to the 'inner' function
          print(x)
     inner()
     print(x)
outer()  
# Because of the enclosing score it will print:
# 'outer_x'
# 'outer_x'
'''
