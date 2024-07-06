x = "global x"

def test():
    y = "local y" #this is local to the function test
    print(y)#first checks for y in the local scope
    print(x)# printed x from within the test() function; first looks for x variable defined within the test function
    #N/B: This doesn't go both ways
test()
print(x)# function can print the x variable within and without


def test(z):
    y = "local y" 
    #print(y)
    print(z)# only local to that test function
test("local z")
#print(x)

#Built-in : are names pre-assigned in python

import builtins

#print(dir(builtins))

def my_min():
    pass

m = min(5, 1, 4, 2, 3)#defines the smallest function of an iterable
print(m)

#nclosing Scope: has to do with nested functions

def outer():
    x = "outer x" #variable local to our outer function

    def inner():
        x = "inner x" # x variable is local to our inner function
        print(x)
    inner()#calls inner function
    print(x)# prints x variable in outer function

outer()#prints everything in the global scope


def outer():
    x = "outer x"

    def inner():
        #x = "inner x"
        print(x) #looks for x in the inner variable but doesn't find it, it looks in any global scope for an enclosing variable
    inner()
    print(x)

outer()

# x variable in the inner function doesn't affect x variable in the global variable
def outer():
    x = "outer x"

    def inner():
        nonlocal x #allows us to work with local variables of enclosing functions; this will affect x variable of the outer function
        x = "inner x"
        print(x) #looks for x in the inner variable but doesn't find it, it looks in any global scope for an enclosing variable
    inner()
    print(x)

outer()



x = "global x"

def outer():
    x = "outer x"

    def inner():
        x = "inner x"
        print(x) #looks for x in the inner variable but doesn't find it, it looks in any global scope for an enclosing variable
    inner()
    print(x)

outer()