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
        if not head:
            return None

        dummy = Node(0)
        tail = dummy
        mapping = {}
        curr_node = head
        while curr_node:
            copy = Node(curr_node.val)
            tail.next = copy
            tail = copy
            mapping[curr_node] = copy

            curr_node = curr_node.next
        
        curr_node = head
        while curr_node:
            if curr_node.random:
                mapping[curr_node].random = mapping[curr_node.random]

            curr_node = curr_node.next

        return dummy.next