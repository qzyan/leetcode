"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr_node = root
        next_start = None
        prev_node = Node()

        while curr_node or next_start:
            if not curr_node:
                curr_node = next_start
                prev_node = Node()
                next_start = None
                continue

            if not next_start:
                next_start = curr_node.left or curr_node.right

            if curr_node.left:
                prev_node.next = curr_node.left
                prev_node = curr_node.left
            if curr_node.right:
                prev_node.next = curr_node.right
                prev_node = curr_node.right

            curr_node = curr_node.next

        return root