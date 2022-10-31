# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        size = self.get_size(head)
        k = k % size
        
        if k == 0:
            return head
        
        left = head
        right = head
        
        for _ in range(k):
            right = right.next 
            
        while right.next:
            left = left.next
            right = right.next 
        
        new_head = left.next
        left.next = None
        right.next = head
        
        return new_head
        
    def get_size(self, head):
        if head is None:
            return 0
        
        curr = head
        size = 0
        
        while curr:
            size += 1
            curr = curr.next
            
        
        return size