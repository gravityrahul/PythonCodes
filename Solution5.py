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
    Name:/home/rahul/Python/LINKEDLISTS/Solution5.py
"""

class Node:
    
    __slots__='element','Next','Prev'
    
    def __init__(self, element, Next, Prev):
        self.element=element
        self.Next=Next
        self.Prev=Prev

    
class DoublyLinkedList(object):
    
    size=0
    Head=None
    Tail=None
    
    def insertElement(self, e):
        
        newNode=Node(e, None, None) # Create a new node with None as tail and head pointer
        
        if DoublyLinkedList.size==0:
            DoublyLinkedList.Head=newNode # Create a newNode and call it Head Reference
            DoublyLinkedList.Tail=DoublyLinkedList.Head # Create a Tail Reference by refering to Head
            
        #Append at the begining of the List if the new item is less than the Head
        elif e < DoublyLinkedList.Head.element:
            newNode.Next=DoublyLinkedList.Head
            DoublyLinkedList.Head.Prev=newNode
            DoublyLinkedList.Head=newNode
            
        #Append at the Tail of the List if the new item is more than the Tail
        elif e > DoublyLinkedList.Tail.element:
            newNode.Prev=DoublyLinkedList.Tail
            DoublyLinkedList.Tail.Next=newNode
            DoublyLinkedList.Tail=newNode
            
        # Else append in the middle
        
        else:
            tempNode=DoublyLinkedList.Head
            while(tempNode and tempNode.element < e):
                tempNode=tempNode.Next
                
            newNode.Next=tempNode
            newNode.Prev=tempNode.Prev
            tempNode.Prev.Next=newNode
            tempNode.Prev=newNode
            
        DoublyLinkedList.size += 1
        
        
    
def reverseDoublyLinkedList(DLLObject):

    startNode=DLLObject.Head
    tempNode=None
    while(startNode):
        # Swap the Next and Previous Nodes
        tempNode=startNode.Next
        startNode.Next=startNode.Prev
        startNode.Prev=tempNode
        if startNode.Prev is None:
            # Head property needs to point to the latest Node
            DLLObject.Head=startNode
        
        # Move onto the next Node (since we just Next and Previous
        startNode=startNode.Prev
    return DLLObject
    
    
            
def  DisplayListTraversal(DLLObject):   
    
    tempHeadNode= DLLObject.Head
    while(tempHeadNode):
        print "Current element = [%d]"%tempHeadNode.element
        tempHeadNode=tempHeadNode.Next


if __name__=="__main__":
    
    DLL = DoublyLinkedList()
    
    nums = [20,14,10,23,12,7,3,2,45,59,87,1,100]

    print "Inserting Elements"
    print "===================================\n"
    for num in nums:
        DLL.insertElement(num)
    
    print "Displaying Elements"
    print "===================================\n"
    DisplayListTraversal(DLL)
    
    ReverseDLL=reverseDoublyLinkedList(DLL)
    
    print "Displaying Elements"
    print "===================================\n"
    DisplayListTraversal(ReverseDLL)
    
        