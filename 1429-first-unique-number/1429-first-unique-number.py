class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.dummy = ListNode(-1)
        self.tail = self.dummy
        self.num_count = {}
        self.num_prev = {}
        
        for num in nums:
            self.add(num)
        
        
    def showFirstUnique(self) -> int:
        if self.dummy.next is None:
            return -1
        
        return self.dummy.next.val

    def add(self, value: int) -> None:
        count = self.num_count.get(value, 0)
        if count == 0:
            node = ListNode(value)
            self.num_prev[value] = self.tail
            self.tail.next = node
            self.tail = node
        elif count == 1:
            prev_node = self.num_prev[value]
            curr_node = prev_node.next
            prev_node.next = curr_node.next
            curr_node.next = None
            
            # node to delete is not the tail
            if prev_node.next:
                self.num_prev[prev_node.next.val] = prev_node
            else:
                # node to delete is the tail
                self.tail = prev_node
            self.num_prev.pop(value)
        
        self.num_count[value] = count + 1
            


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)