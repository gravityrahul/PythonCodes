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
    Date:Jun 7, 2014
    Name:/home/rahul/Python/LINKEDLISTS/Solution1.py
    
    Please Consult README for the Question, the solution provided here is more generic 
    than just inserting 40 in the middle.
    
    Let's do some time complexity 
    
    Worst Case: If the element being inserted is new maximum and since there is no tail reference O(n)
    Best Case: If the element is new minimum, then O(1) insertion at Head.
"""

class Node:

    """
    Basic Node Object
    """    
    __slots__ = 'elements', 'Next'
    
    def __init__(self, element, Next):
        self.element = element
        self.Next=Next
        
        
class LinkedList(object):

    """
    Create a linkedlist object using the Node Object
    """
    size = 0 # Let size be the attribute of the LinkedList Class Object
    
    def __init__(self):
        
        """
        Initialize a Head reference of the LinkedList object
        """
        self.Head=None
        
    def addElement(self, e):
        
        # Create a newNode Object
        newNode = Node(e, None)
        if LinkedList.size==0:
            self.Head=newNode
        else:
            newNode.Next=self.Head
            self.Head=newNode
        LinkedList.size += 1
        
    def displayList(self):
        #Create a tempNode and iterate
        tempNode = self.Head
        while(tempNode):
            print "Current element is [%d]"% tempNode.element
            tempNode = tempNode.Next
        
    
    def addElementinOrder(self, e):
        # Create a slow pointer and a Fast pointer
        # Travel through the list and place the element 
        # immediately after the element smaller than the given 
        # element.
        # We will also address the edge cases here
        
        slowNode=self.Head
        fastNode=self.Head.Next
        newNode = Node(e,None)
        # Check if the element that is added is less than the head
        # Add the element in head
        if self.Head.element > e:
            self.addElement(e)
        # Travel until you reach dead end
        else:
            while(fastNode):
                #stop traversing as soon as you find element larger than target
                if fastNode.element > e:
                    break
                else:
                # Continue traversing otherwise
                    slowNode=slowNode.Next
                    fastNode=fastNode.Next  
            #Make changes to the node 
            newNode.Next=fastNode
            slowNode.Next=newNode
                
        
    
    
    
if __name__== "__main__":
    
    MyLinkedList = LinkedList()
    nums = [70, 60, 50, 30, 20, 10]
    for n in nums:
        print "Inserting num = %d" % n
        MyLinkedList.addElement(n)
    
    print "=================================\n"
    print "Displaying elements in LinkedList"
    MyLinkedList.displayList()
    
    print "=================================\n"
    print "The Length of LinkedList is %d" % MyLinkedList.size
    
    print "=================================\n"
    print "Inserting 40 in LInkedList"
    
    MyLinkedList.addElementinOrder(40)
    
    print "Displaying elements in LinkedList"
    MyLinkedList.displayList()