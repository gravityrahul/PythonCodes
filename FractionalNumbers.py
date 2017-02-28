'''
Implements a irrational number adder

a/b + c/d = (ad + bc)/bd

'''

class IrrationalNumber(object):
    '''
    classdocs
    '''


    def __init__(self, numerator, denominator):
        '''
        Constructor
        '''
        self.numerator = numerator
        self.denominator = denominator
        
    def __add__(self, other_irrational):
        '''
        adder function
        '''
        numerator = self.numerator*other_irrational.denominator + other_irrational.numerator*self.denominator
        denominator = self.denominator*other_irrational.denominator
        gcd = self.__GCD__(numerator, denominator)
        return IrrationalNumber(numerator/gcd, denominator/gcd)
    
    def __sub__(self, other_irrational):
        '''
        difference function
        '''
        numerator = self.numerator*other_irrational.denominator - other_irrational.numerator*self.denominator
        denominator = self.denominator*other_irrational.denominator
        gcd = self.__GCD__(numerator, denominator)
        return IrrationalNumber(numerator/gcd, denominator/gcd)
    
    def __mul__(self, other_irrational):
        '''
        product 
        '''
        numerator = self.numerator*other_irrational.numerator
        denominator = self.denominator*other_irrational.denominator
        gcd = self.__GCD__(numerator, denominator)
        return IrrationalNumber(numerator/gcd, denominator/gcd)
    
    def __repr__(self):
        return str(self.numerator) + '/' + str(self.denominator)
    
    def __GCD__(self, numerator, denominator):
        p = numerator
        q = denominator
        while(p!=q):
                if p < q:
                    p, q = q, p
                else:
                    p=p-q
        return p
        

irrnum1 = IrrationalNumber(2,3)
irrnum2 = IrrationalNumber(5,6)
        
print irrnum1
print irrnum2

print irrnum1 + irrnum2

print irrnum1 * irrnum2