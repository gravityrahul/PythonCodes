'''
Created on Dec 31, 2013

@author: 502100330
'''
o = object
class F(o):pass
class D(o):pass
class E(o):pass
class C(D,F):pass
class B(E,D):pass
class A(B,C):pass

print A.mro()