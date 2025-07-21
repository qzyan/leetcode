# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        size = 1
        dummy = ListNode()
        dummy.next = head
        curr_node = head
        prev_node = dummy
        while curr_node:
            last_node, group_size = self.get_last_node(curr_node, size)
            if group_size % 2 == 1:
                prev_node = last_node
                curr_node = last_node.next
                size += 1
            else:
                next_node = last_node.next
                last_node.next = None
                self.reverse(curr_node, last_node)
                prev_node.next = last_node
                prev_node = curr_node
                curr_node.next = next_node
                curr_node = next_node
                size += 1

        return dummy.next

    def reverse(self, head, tail):
        prev_node = None
        node = head
        while node:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node

    def get_last_node(self, head, size):
        k = 1
        while head.next:
            if k == size:
                break
            
            k += 1
            head = head.next
        
        return head, k
            



