class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.dummy = ListNode(-1)
        self.tail = self.dummy
        self.unique_val_prev = {}
        self.dups = set()
        
        for num in nums:
            self.add(num)
        

    def showFirstUnique(self) -> int:
        if self.dummy.next:
            return self.dummy.next.val
        return -1

    def add(self, value: int) -> None:
        if value in self.dups:
            return
        
        # value was unique, with current add, is no more unique 
        if value in self.unique_val_prev:
            # remove the node from linked list
            prev_node = self.unique_val_prev[value]
            curr_node = prev_node.next
            print(prev_node.val, curr_node.val)
            prev_node.next = curr_node.next
            # if the curr is tail, move the tail forward
            if self.tail == curr_node:
                self.tail = prev_node
            # curr is not tail, update the unique_val_prev[next_node.val]
            else:
                next_val = curr_node.next.val
                self.unique_val_prev[next_val] = prev_node
                
            # remove it from unique_val_prev
            self.unique_val_prev.pop(value)
            # add it to dups
            self.dups.add(value)
            return
        
        # value was never before
        curr_node = ListNode(value)
        self.tail.next = curr_node
        self.unique_val_prev[value] = self.tail
        self.tail = curr_node
        return

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)