"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        
        node_dict = {}
        curr = head
        dummy = Node(-1, None, None)
        copied_prev = dummy
        
        while curr:
            copied = Node(curr.val, None, None)
            copied_prev.next = copied
            
            node_dict[curr] = copied
            curr = curr.next
            copied_prev = copied
            
        curr = head
        curr_copied = dummy.next
        while curr:
            if not curr.random:
                curr = curr.next
                curr_copied = curr_copied.next
                continue
                
            curr_copied.random = node_dict[curr.random]
            curr = curr.next
            curr_copied = curr_copied.next
            
        return dummy.next
            
            
            
            
            