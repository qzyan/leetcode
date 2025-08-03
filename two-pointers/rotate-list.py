# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        size = self.get_size(head)
        k = k % size

        if k == 0:
            return head

        dummy = ListNode()
        dummy.next = head
        node = head
        prev_node = head
        while k:
            node = node.next
            k -= 1

        # node is the last node
        # prev_node is the new tail
        while node.next:
            node = node.next
            prev_node = prev_node.next

        node.next = dummy.next

        dummy.next = prev_node.next
        prev_node.next = None

        return dummy.next

    def get_size(self, head):
        size = 0
        while head:
            size += 1
            head = head.next

        return size
