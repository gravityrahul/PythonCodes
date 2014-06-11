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
    Name:/home/rahul/Python/LINKEDLISTS/Solution4.py
"""

class Node:
    
    __slots__='element', 'Next'
    
    def __init__(self, element, Next):
        self.element = element
        self.Next = Next
        
    

class LinkedList(object):
    
    #Let size of the Linked List and Head Pointer be the attribute of
    # the Linked List. Why? Because given the Linked List, we shall have 
    # the knowledge of the Head
    size=0
    Head=None 
        
    def addElement(self, e):
        
        # Create a newNode Object
        newNode = Node(e, None)
        if LinkedList.size==0:
            LinkedList.Head=newNode
        else:
            newNode.Next=LinkedList.Head
            LinkedList.Head=newNode
        LinkedList.size += 1
        
    def displayList(self):
        #Create a tempNode and iterate
        tempNode = LinkedList.Head
        while(tempNode):
            print "Current element is [%d]"% tempNode.element
            tempNode = tempNode.Next
   
##################################################################
# Function to get the last but fifth element in the LinkedList
################################################################## 
    
def YieldNthElementFromEnd(LinkedListObject, size, n):
    
    nIndex = LinkedListObject.size - n
    tempNode = LinkedListObject.Head
    c=0
    while(c < nIndex):
        tempNode=tempNode.Next
        c +=1
    return tempNode.element
            


def YieldNthElement(LLObject):
    
    slowNode=LLObject.Head
    fastNode=LLObject.Head.Next.Next.Next.Next.Next
    while(fastNode):
        slowNode=slowNode.Next
        fastNode=fastNode.Next
    return slowNode.element
        
    


if __name__=="__main__":
    
    MLL = LinkedList()
    
    nums = [4,5,8,1,2,3,4,5,6,7,10,12,13]
    for num in nums:
        MLL.addElement(num)
        
    MLL.displayList()
    
    NthElement = YieldNthElementFromEnd(MLL, MLL.size, 5)
    print NthElement
    
    print YieldNthElement(MLL)
    
    