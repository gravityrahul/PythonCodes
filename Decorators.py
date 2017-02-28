'''
Decorators can be used to "wrap" a function with another function.
When implementing a decorator, it is helpful to remember that the following decorator
application:
@dec
def func(arg1, arg2):
    pass

is equivalent to

def func(arg1, arg2):
    pass
func = dec(func)
'''
def trace(func):
    def inner(*args, **kwargs):
        print "Inside main function tracer"
        print '>>'
        func(*args, **kwargs)
        print '<<'
    return inner
        
@trace
def g(x,y):
    print "Inside function g"
    print 'x:', x, 'y:' ,y
    
@trace
def square(x):
    print x*x

    
#Decorator with arguments
def tracewithMessage(msg):                #Main function
    print msg
    def inner(func):                      # First nested function
        print "Inside first inner"
        def innerinner(*args, **kwargs):  #Second nested function
            print "Inside second inner"
            print '>>'
            func(*args, **kwargs)
            print '<<'
        return innerinner
    return inner

@tracewithMessage('Trace with message')
def cube(x):
    print "Inside cube"
    print  x*x*x

def test():
    #g('2','3')
    #square(4)
    cube(5)
    
if __name__=='__main__':
    test()
        