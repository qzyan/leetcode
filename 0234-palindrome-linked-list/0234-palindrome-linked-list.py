# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        
        
        # reversed the half of the LinkedList
        second_half_head = self.find_second_half_head(head)
        reversed_head = self.reverse_the_second_half(head, second_half_head)
        
        left = head
        right = reversed_head
        while right is not None:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next 
           
        return True

            
    def find_second_half_head(self, head):
        slow = head
        fast = head 
        
        while fast is not None and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next 
        
        return slow if fast is None else slow.next 
            
    def reverse_the_second_half(self, head, second_half_head):
        prev = None 
        curr = second_half_head
        
        while curr is not None:
            next_temp = curr.next 
            curr.next = prev
            
            prev = curr
            curr = next_temp
        
        return prev
        
        
        
        
        
        
        """
        # reversed the whole linkedList to see it is the same with the origin one
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
        """
