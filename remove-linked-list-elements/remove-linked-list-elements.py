# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
             return head
        
        dummy = ListNode()
        dummy.next = head
        curr_node = dummy.next
        prev_node = dummy
        
        while curr_node:
            if curr_node.val != val:
                prev_node = curr_node
                curr_node = curr_node.next
                continue
            
            if curr_node.val == val:
                prev_node.next = curr_node.next
                curr_node = curr_node.next
        
        return dummy.next