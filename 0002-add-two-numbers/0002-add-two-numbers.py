# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        needPlusOne = False
        dummy = ListNode()
        curr = dummy
        
        while l1 or l2:
            val_l1 = l1.val if l1 is not None else 0
            val_l2 = l2.val if l2 is not None else 0
            val = val_l1 + val_l2 + (1 if needPlusOne else 0)
            if val >= 10:
                val = val - 10
                needPlusOne = True
            else:
                needPlusOne = False
            
            node = ListNode(val)
            curr.next = node
            curr= curr.next 
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            
        if needPlusOne:
            node = ListNode(1)
            curr.next = node
            
        return dummy.next 