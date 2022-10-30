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
        
        self.flatten_dfs(head)
        
        return head 
    
    def flatten_dfs(self,head):
        # return the tail of the linkedlist
        if head.next is None and head.child is None:
            return head
    
        child_node = head.child 
        next_node = head.next 
        child_tail = None
        next_tail = None
        head.child = None
        
        if child_node:
            head.next = child_node
            child_tail = self.flatten_dfs(child_node)
            child_node.prev = head
            
        if next_node:
            next_tail = self.flatten_dfs(next_node)
            if child_tail:
                child_tail.next = next_node
                next_node.prev = child_tail
        
        return next_tail or child_tail
