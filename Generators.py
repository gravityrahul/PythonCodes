'''
Created on Mar 15, 2014

@author: 502100330
'''
def my_generator():
    try:
        yield 'something'
    except ValueError:
        yield 'dealing with the exception'
    finally:
        print "ok let's clean"
        
gen=my_generator()

gen.throw(ValueError('mean'))