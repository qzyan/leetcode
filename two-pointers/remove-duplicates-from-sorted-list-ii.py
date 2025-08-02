# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        curr_node = head
        prev_node = dummy
        while curr_node:
            
            # the curr_node is a unique val
            if curr_node.next is None or curr_node.val != curr_node.next.val:
                prev_node = curr_node
                curr_node = curr_node.next
                continue

            # curr_node is not a unique val, go the the last of the same val
            while curr_node.next and curr_node.val == curr_node.next.val:
                curr_node = curr_node.next

            prev_node.next = curr_node.next
            curr_node = curr_node.next

        return dummy.next
            