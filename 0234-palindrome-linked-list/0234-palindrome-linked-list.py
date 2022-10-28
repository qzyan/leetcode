# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reversed_dummy_head = ListNode(0)
        curr_node = head
        
        while curr_node:
            copied_node = ListNode(curr_node.val)
            copied_node.next = reversed_dummy_head.next 
            reversed_dummy_head.next = copied_node
            
            curr_node = curr_node.next 
        
        curr_reversed_node = reversed_dummy_head.next 
        curr_node = head
                
        while curr_node:
            if curr_reversed_node.val != curr_node.val:
                return False 
            
            curr_node = curr_node.next 
            curr_reversed_node = curr_reversed_node.next
            
        return True