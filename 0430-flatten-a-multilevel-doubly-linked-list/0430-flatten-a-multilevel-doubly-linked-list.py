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
        
        stack = []
        stack.append(head)
        dummy = Node(0, None, head, None)
        prev = dummy
        
        while stack:
            node = stack.pop()
            
            prev.next = node
            node.prev = prev
            
            if node.next:
                stack.append(node.next)
            
            if node.child:
                stack.append(node.child)
                node.child = None
                
            prev = node
            
        head.prev = None
        
        return head
                
            
