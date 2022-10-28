# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head
        
        odd_start = head
        even_start = head.next

        curr_odd = odd_start
        curr_even = even_start
        
        while curr_even and curr_even.next:
            next_even = curr_even.next.next
            next_odd = curr_odd.next.next 
            curr_odd.next = next_odd
            curr_even.next = next_even
            
            curr_even = next_even
            curr_odd = next_odd
            
        curr_odd.next = even_start
        
        
        return odd_start
    
        