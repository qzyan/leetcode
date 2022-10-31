"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.node_dict = {}
        
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        curr = head
        while curr:
            copied_node = Node(curr.val, None, None)
            
            copied_node.next = curr.next
            curr.next = copied_node
            
            curr = curr.next.next 
        
        curr = head
        
        while curr:
            curr.next.random = curr.random.next if curr.random else None 
            
            curr = curr.next.next 
            
        curr = head
        copied_curr = curr.next 
        copied_head = copied_curr
        
        while curr:
            curr.next = copied_curr.next 
            copied_curr.next = copied_curr.next.next if copied_curr.next else None
            
            curr = curr.next 
            copied_curr = copied_curr.next 
        
        return copied_head
        
            