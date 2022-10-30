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
        
        dummy = Node(0, None, head, None)
        self.flatten_dfs(head, dummy)
        
        head.prev = None
        dummy.next = None
        
        return head 
    
    # return the tail of the linkedlist
    def flatten_dfs(self,head, prev_node):
        if head is None:
            return prev_node
        
        
        child_node = head.child 
        next_node = head.next
        head.prev = prev_node
        prev_node.next = head  
        
        child_node_tail = self.flatten_dfs(child_node, head)
        next_node_tail = self.flatten_dfs(next_node, child_node_tail)
        
        head.child = None
        
        return next_node_tail
