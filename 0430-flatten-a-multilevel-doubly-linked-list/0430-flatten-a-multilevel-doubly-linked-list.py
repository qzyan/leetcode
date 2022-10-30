"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        curr = head
        while curr:
            child_head = self.flatten(curr.child)
            
            if child_head:
                self.append_after(curr, child_head)
                curr.child = None
            
            curr = curr.next
        
        return head
    
    def append_after(self, node, head):
        tail = self.find_tail(head)
        next_node = node.next 
        
        if next_node is None:
            node.next = head
            head.prev = node
            return 
        
        node.next = head
        next_node.prev = tail
        
        head.prev = node
        tail.next = next_node
    
    def find_tail(self, head):
        if head is None:
            return None
        
        curr = head
        prev = None
        
        while curr:
            prev = curr
            curr = curr.next 
            
        return prev
            