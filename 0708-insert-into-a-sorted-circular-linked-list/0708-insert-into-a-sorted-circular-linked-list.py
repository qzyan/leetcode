"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node_to_insert = Node(insertVal)
        if head is None:
            node_to_insert.next = node_to_insert
            return node_to_insert
        
        if head.next is None:
            head.next = node_to_insert
            node_to_insert.next = head 
            return head
        
        prev = head
        curr = head.next 
        
        is_iterate_all = False
        
        while not is_iterate_all:
            if curr == head:
                is_iterate_all = True
        
            if curr.val > prev.val and insertVal <= curr.val and insertVal >= prev.val:
                node_to_insert.next = curr
                prev.next = node_to_insert
                return head 
            
            if curr.val < prev.val and (insertVal >= prev.val or insertVal <= curr.val):
                node_to_insert.next = curr
                prev.next = node_to_insert
                return head 
            
            if curr.val == prev.val and insertVal == curr.val and insertVal == prev.val:
                node_to_insert.next = curr
                prev.next = node_to_insert
                return head 
                        
            prev = curr
            curr = curr.next 
        
        node_to_insert.next = curr
        prev.next = node_to_insert
        
        return head