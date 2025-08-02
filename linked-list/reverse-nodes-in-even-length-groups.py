# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        group_idx = 1
        curr_node = head
        prev_node = None

        while curr_node:
            tail, size = self.get_tail(curr_node, group_idx)
            if size % 2 != 0:
                curr_node = tail.next
                prev_node = tail
                group_idx += 1
                continue

            next_head = tail.next
            # split
            tail.next = None
            self.reverse(curr_node)
            # link with prev group tail
            prev_node.next = tail
            prev_node = curr_node
            # link with next group
            prev_node.next = next_head

            curr_node = next_head
            group_idx += 1

        return head

    def get_tail(self, curr_node, k):
        node = curr_node
        size = 1
        while node.next and size < k:
            node = node.next
            size += 1

        return node, size

    def reverse(self, node):
        prev_node = None

        while node:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node


        




            

