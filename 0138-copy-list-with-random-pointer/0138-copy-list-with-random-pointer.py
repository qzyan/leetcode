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
        
        if head in self.node_dict:
            return self.node_dict[head]
        
        new_node = Node(head.val, None, None)
        self.node_dict[head] = new_node
        
        new_node.next = self.copyRandomList(head.next)
        new_node.random = self.copyRandomList(head.random)
        
        return new_node
            