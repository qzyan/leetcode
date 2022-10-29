# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:  
        if list1 is None:
            return list2
        if list2 is None:
            return list1        
        
        dummy_head = ListNode()
        dummy_head.next = list2
        curr_1 = list1
        curr_2 = list2
        prev = dummy_head 
        
        while curr_1 and curr_2:
            if curr_1.val < curr_2.val:
                prev.next = curr_1
                prev = curr_1
                curr_1 = curr_1.next 
                prev.next = curr_2
                continue 
            
            prev.next = curr_2
            prev = curr_2
            curr_2 = curr_2.next 
        
        while curr_1 is not None:
            prev.next = curr_1
            prev = curr_1
            curr_1 = curr_1.next 
            
        return dummy_head.next 