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
    Name:/home/rahul/Python/LINKEDLISTS/Solution1B.py
    
    A self sorting LinkedList 
    Time Complexity Worst Case O(n)
"""

class Node:
    """
    Create  node object
    """
    __slots__='elements', 'Next'
    
    def __init__(self, element, Next):
        self.element=element
        self.Next=Next
        

class SortedLL(object):
    """
    Create a sorted LinkedList Structure using Node object
    """
    
    size=0 # size be the attribute of the SLL object
    
    def __init__(self):
        self.Head=None
        self.Tail=None
        
    def addElementHead(self, e):
        newNode = Node(e, None)
        if SortedLL.size==0:
            self.Head=newNode
            self.Tail=newNode
        else:
            newNode.Next=self.Head
            self.Head=newNode
        SortedLL.size +=1
               
             
    def addElement(self, e):
        
        # If initial size is 0 we can start by Head or Tail
        # Let's start by Head
        if (SortedLL.size==0 or e < self.Head.element):
            self.addElementHead(e)
        else:
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
            SortedLL.size +=1
            
    def displayList(self):
        #Create a tempNode and iterate
        tempNode = self.Head
        while(tempNode):
            print "The element is [%d]"% tempNode.element
            tempNode = tempNode.Next
        


MySortedLL = SortedLL()

nums = [20,14,10,23,12,7,3,2,45,59,87,1,100]

print "===================================\n\n"
for num in nums:
    print "Inserting number [%d] in LinkedList"%num
    MySortedLL.addElement(num)
    
print "===================================\n\n"
MySortedLL.displayList()
