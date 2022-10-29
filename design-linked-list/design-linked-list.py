class DoublyLinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        node = self.getNodeAtIndex(index)
        if node is None:
            return -1
        
        return node.val

    def addAtHead(self, val: int) -> None:
        curr_node = DoublyLinkedListNode(val)
        next_node = self.head
        
        if next_node is None:
            self.head = curr_node
            return
        
        curr_node.next = next_node
        next_node.prev = curr_node
        self.head = curr_node
        
    def addAtTail(self, val: int) -> None:
        curr_node = DoublyLinkedListNode(val)
        prev_node = self.getTail()
        
        if prev_node is None:
            self.head = curr_node
            return
        
        prev_node.next = curr_node
        curr_node.prev = prev_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return 
        
        prev_node = None
        curr_node = self.head
        curr_index = 0
        
        while curr_index < index:
            if curr_node is None:
                return 
            
            prev_node = curr_node
            curr_node = curr_node.next
            curr_index += 1
        
        if curr_node is None:
            self.addAtTail(val)
            return
            
        new_node = DoublyLinkedListNode(val)
        new_node.prev = prev_node
        new_node.next = curr_node
        prev_node.next = new_node
        curr_node.prev = new_node

    def deleteAtIndex(self, index: int) -> None:
        node_to_delete = self.getNodeAtIndex(index)
        if node_to_delete is None:
            return 
        
        if node_to_delete.prev is None and node_to_delete.next is None:
            self.head = None
            return
        
        if node_to_delete.prev is None and node_to_delete.next is not None:
            self.head = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev
            return 
        
        if node_to_delete.prev is not None and node_to_delete.next is None:
            node_to_delete.prev.next = None
            return 
        
        node_to_delete.prev.next = node_to_delete.next
        node_to_delete.next.prev = node_to_delete.prev
    
        
        
        
    def getTail(self):
        curr = self.head
        while curr is not None and curr.next is not None:
            curr = curr.next
        
        return curr
        
    def getNodeAtIndex(self, index):
        curr = self.head
    
        curr_index = 0
        
        while curr is not None and curr_index < index:
            curr = curr.next
            curr_index += 1
            
        return curr
    

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)