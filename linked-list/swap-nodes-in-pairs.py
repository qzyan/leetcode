# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        curr_node = head
        prev_node = dummy
        while curr_node:
            next_node = self.split(curr_node)

            new_head = self.reverse(curr_node)
            prev_node.next = new_head
            prev_node = curr_node

            curr_node = next_node

        return dummy.next

    def split(self, node):
        if node.next is None:
            return None

        new_head = node.next.next
        node.next.next = None
        return new_head

    def reverse(self, node):
        prev_node = None
        while node:
            next_node = node.next
            node.next = prev_node

            prev_node = node
            node = next_node

        return prev_node