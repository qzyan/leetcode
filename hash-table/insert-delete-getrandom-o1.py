class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.val_idx_mapping = {}
        

    def insert(self, val: int) -> bool:
        if val in self.val_idx_mapping:
            return False
        
        self.val_idx_mapping[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_idx_mapping:
            return False

        if self.val_idx_mapping[val] == len(self.vals) - 1:
            self.vals.pop()
            self.val_idx_mapping.pop(val)
            return True

        val_idx = self.val_idx_mapping[val]
        last_val = self.vals[-1]
        self.val_idx_mapping[last_val] = val_idx
        self.vals[val_idx] = last_val

        self.vals.pop()
        self.val_idx_mapping.pop(val)
        return True

    def getRandom(self) -> int:
        idx = int(len(self.vals) * random.random())
        return self.vals[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()