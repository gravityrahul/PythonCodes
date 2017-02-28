'''
Created on Jan 31, 2014

@author: 502100330
'''

def GreatestCommonDivisor(p,q):
        while(p!=q):
                if p < q:
                    p, q = q, p
                else:
                    p=p-q
        return p
        
gcd = GreatestCommonDivisor(10, 25)
print gcd