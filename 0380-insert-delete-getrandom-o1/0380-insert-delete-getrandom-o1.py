import random

class RandomizedSet:

    def __init__(self):
        self.appeared_to_index = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.appeared_to_index:
            return False
        
        self.nums.append(val)
        self.appeared_to_index[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.appeared_to_index:
            return False
        
        index = self.appeared_to_index[val]
        last_val = self.nums[-1]
        self.nums[index] = last_val
        self.appeared_to_index[last_val] = index
        self.appeared_to_index.pop(val)
        self.nums.pop()
        
        return True
        
    def getRandom(self) -> int:
        random_idx = random.randint(0, len(self.nums) - 1)
        return self.nums[random_idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()