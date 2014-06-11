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
    Name:/home/rahul/Python/LINKEDLISTS/Solution6.py
"""
class Node:
    
    __slots__='element', 'Next'
    
    def __init__(self, element, Next):
        self.element=element
        self.Next=Next
        

class LinkedList(object):
    
    size=0 #attribute of the class
    Head=None
    Tail=None
    
    def insertElement(self, e):
        
        # Insert a new node 
        newNode=Node(e, None)
        
        if LinkedList.size==0:
            LinkedList.Head=newNode
            LinkedList.Tail=newNode
        else:
            newNode.Next=LinkedList.Head
            LinkedList.Head=newNode
        LinkedList.size += 1
        
        
        
def displayList(LLObject):
    
    tempNode=LLObject.Head
    while(tempNode):
        print "Current Element is [%d]"%(tempNode.element)
        tempNode =tempNode.Next
    
    
def AppendNElementsHead(LLObject, n):
    """
    Given a Linked List object, append the last n elements to head
    """
    n_remaining=LLObject.size - n # Count the number of Nodes required to shift from Head
    tempNode=LLObject.Head # Point a tempNode to Head
    c=0
    while(c < n_remaining):
        LLObject.Tail.Next=tempNode # Point the Next of tail to tempNode
        LLObject.Tail=tempNode # Declare the tempNode as new Tail
        LLObject.Head=LLObject.Head.Next # Move the Head by one pointer
        tempNode=LLObject.Head # Reassign the new head as tempNode
        c+=1 #Increase the counter
        
    LLObject.Tail.Next=None # At this point, the above linkage is circular, hence break the linkage
        
    return LLObject
    
 
    
if __name__=="__main__":
    
    MLL=LinkedList()
    nums = [6, 5,4,3,2,1]
    for n in nums:
        print "Inserting num = %d" % n
        MLL.insertElement(n)
    
    print "=================================\n"
    print "Displaying elements in LinkedList"
    displayList(MLL)
    
    MLL_new = AppendNElementsHead(MLL, 2)
    
    print "=================================\n"
    print "Displaying elements in Appened LinkedList"
    displayList(MLL_new)
    
    