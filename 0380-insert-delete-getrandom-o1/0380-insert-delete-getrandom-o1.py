import random
class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.val_index_mapping = {}
                

    def insert(self, val: int) -> bool:
        if val in self.val_index_mapping:
            return False
        
        self.vals.append(val)
        self.val_index_mapping[val] = len(self.vals) - 1
        
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.val_index_mapping:
            return False
        
        index = self.val_index_mapping[val]
        last_val = self.vals[len(self.vals) - 1]
        
        self.vals[index] = last_val
        self.val_index_mapping[last_val] = index
        
        self.val_index_mapping.pop(val)
        self.vals.pop()
        
        return True

    def getRandom(self) -> int:
        size = len(self.vals)
        index = random.randint(0, size - 1)
        return self.vals[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()