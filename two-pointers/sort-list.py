# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        size = self.get_size(head)
        partition_len = 1
        while partition_len < size:
            self.partition_and_sort(dummy, partition_len)
            partition_len *= 2

        return dummy.next

    def get_size(self, head):
        size = 0
        while head:
            size += 1
            head = head.next
        
        return size

    def partition_and_sort(self, dummy, partition_len):
        prev = dummy
        head = prev.next
        while head:
            next_head = self.get_next_head(head, partition_len)
            node1, node2 = self.partition(head, partition_len)
            new_head, new_tail = self.merge(node1, node2)
            prev.next = new_head
            prev = new_tail
            head = next_head

    def get_next_head(self, head, partition_len):
        for _ in range(partition_len * 2):
            if not head:
                break
            head = head.next
        
        return head

    def partition(self, head, partition_len):
        node1 = head
        node2 = head
        idx = 0
        while node2 and idx < partition_len:
            node2 = node2.next
            idx += 1

        idx = 0
        tail1 = node1
        while tail1 and idx < partition_len - 1:
            tail1 = tail1.next
            idx += 1
        if tail1:
            tail1.next = None
        
        idx = 0
        tail2 = node2
        while tail2 and idx < partition_len - 1:
            tail2 = tail2.next
            idx += 1

        if tail2:
            tail2.next = None

        return node1, node2

    def merge(self, node1, node2):
        dummy = ListNode()
        tail = dummy
        while node1 and node2:
            if node1.val <= node2.val:
                tail.next = node1
                node1 = node1.next
            else:
                tail.next = node2
                node2 = node2.next
            tail = tail.next
        
        while node1:
            tail.next = node1
            node1 = node1.next
        
            tail = tail.next
        
        while node2:
            tail.next = node2
            node2 = node2.next

            tail = tail.next
        
        return dummy.next, tail

