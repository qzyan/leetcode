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
        curr_node = head
        while curr_node:
            next_node = curr_node.next
            copy_node = Node(curr_node.val)
            
            curr_node.next = copy_node
            copy_node.next = next_node

            curr_node = next_node
        
        curr_node = head
        while curr_node:
            copy_node = curr_node.next
            random_node = curr_node.random
            if random_node:
                copy_node.random = random_node.next

            curr_node = copy_node.next

        dummy = Node(0)
        tail = dummy
        curr_node = head
        while curr_node:
            copy_node = curr_node.next
            next_node = copy_node.next

            tail.next = copy_node
            tail = copy_node

            if next_node:
                copy_node.next = next_node.next

            curr_node.next = next_node
            curr_node = next_node

        return dummy.next




