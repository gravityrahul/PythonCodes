"""

    Copyright (C) 2014: Rahul Biswas

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    
    Author: Rahul Biswas, <gravityrahul@gmail.com>
    Date:Jun 10, 2014
    Name:/home/rahul/Python/LINKEDLISTS/Solution7.py
"""

from Solution6 import LinkedList, displayList

class LinkedLIST(LinkedList):
    
    pass



def ReturnAlternateNodes(LL_x, LL_y):
    
    """
    Given two LinkedList, return a linked list with alternate pairs
    """
    xtempNode=LL_x.Head
    #ytempNode=LL_y.Head
    while(LL_x.Head and LL_y.Head):
        xtempNode.Next=LL_y.Head
        LL_x.Head = LL_x.Head.Next
        xtempNode.Next=LL_x.Head
        LL_y.Head=LL_y.Head.Next
        
    return xtempNode

if __name__== "__main__":
    
    LL1 = LinkedLIST()
    LL2 = LinkedLIST()
    nums1 = [70, 60, 50]
    nums2= [30, 20, 10]
    for n in nums1:
        print "Inserting num = %d" % n
        LL1.insertElement(n)
    
    for n in nums2:
        print "Inserting num = %d" % n
        LL2.insertElement(n)
    
    
    pairLL=ReturnAlternateNodes(LL1, LL2)
    
    displayList(pairLL)
    
    