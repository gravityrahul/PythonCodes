'''
Exercises:
1. Implement a class that keeps a running total of the number of instances created.
2. Implement another solution to the same problem (a class that keeps a running
total of the number of instances), but this time use a static method instead of a
class method.
'''

class CountInstances(object):

    """
    We use a class variable named instance_count, rather than an instance
    variable, to keep a running total of instances. Then, we increment that variable
    each time an instance is created:
    """
    instance_count = 0
    def __init__(self, name='noname'):
        self.name = name
        CountInstances.instance_count += 1

    def show(self):
        print 'name: "%s"' % (self.name, )

    @classmethod
    def show_instance_count(cls):
        print 'instance count: %d' %(cls.instance_count, )
        
        
class CountInstances2(object):

    """
    Use a static method
    """
    instance_count = 0
    def __init__(self, name='noname'):
        self.name = name
        CountInstances2.instance_count += 1

    def show(self):
        print 'name: "%s"' % (self.name, )

    @staticmethod
    def show_instance_count():
        print 'instance count: %d' %(CountInstances2.instance_count, )
        
def test():
    instances = []
    instances.append(CountInstances('apple'))
    instances.append(CountInstances('banana'))
    instances.append(CountInstances('cherry'))
    instances.append(CountInstances())
    for instance in instances:
        instance.show()
    CountInstances.show_instance_count()
    
def test2():
    instances = []
    instances.append(CountInstances2('apple'))
    instances.append(CountInstances2('banana'))
    instances.append(CountInstances2('cherry'))
    instances.append(CountInstances2())
    for instance in instances:
        instance.show()
    CountInstances2.show_instance_count()
   
    
if __name__ == '__main__':
    test()
    test2()