# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        
        # flip the second half 
        # compare the first half with the second half
        # flip the second half back
        
        # reversed the half of the LinkedList
        first_half_tail = self.find_first_half_tail(head)
        reversed_head = self.reverse_the_second_half(first_half_tail.next)
        
        left = head
        right = reversed_head
        result = True
        
        while right is not None:
            if left.val != right.val:
                result = False
            
            left = left.next
            right = right.next 
           
        self.reverse_the_second_half(reversed_head)
        
        return result 

            
    def find_first_half_tail(self, head):
        slow = head
        fast = head 
        
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next 
            fast = fast.next.next 
        
        return slow
            
    def reverse_the_second_half(self, second_half_head):
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
