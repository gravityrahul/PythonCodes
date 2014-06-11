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
    Name:/home/rahul/Python/LINKEDLISTS/Solution2.py
"""

class Node:
    """
    Create a Node Object
    """
    __slots__= 'element', 'Next'
    
    def __init__(self, element, Next):
        self.element=element
        self.Next=Next
        
class LinkedList(object):
    
    size=0
    hashTableOfElements={} # Create a dict object to see if duplicates exist 
    
    def __init__(self):
        self.Head=None
        
    def addElements(self,e):
        # Primarily add elements in the Head
        newNode = Node(e, None)
        if LinkedList.size==0:
            self.Head=newNode
        else:
            newNode.Next=self.Head
            self.Head=newNode
        LinkedList.size += 1
    
    def removeDuplicates(self):
        # RemoveDuplicates traversing the list in O(n)
        slowNode=self.Head
        fastNode=self.Head.Next
        while(fastNode):
            if not LinkedList.hashTableOfElements.has_key(fastNode.element):
                LinkedList.hashTableOfElements[fastNode.element]=1 
            else:
                slowNode.Next=fastNode.Next
                LinkedList.size -= 1
            slowNode=slowNode.Next
            fastNode=fastNode.Next
        
    
    def displayList(self):
        tempNode=self.Head
        while(tempNode):
            print "Elements in the List are [%d] " %tempNode.element
            tempNode=tempNode.Next
            
        
    
if __name__=="__main__":
    
    MLL = LinkedList()
    
    nums = [1,4,5,8,1,2,3,4,5,6,7,10,12,13,15,46,54,23,12,10,9,8,4,2]
    for num in nums:
        MLL.addElements(num)
        
    #MLL.displayList()
    print "Size Before \n"
    print MLL.size
    
    print "Removing Duplicates"
    MLL.removeDuplicates()
    
    #print "===========================================\n\n"
    #MLL.displayList()
    
    print "Size After \n"
    print MLL.size
    
    
    