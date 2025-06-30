class RandomizedCollection:

    def __init__(self):
        self.vals = []
        self.val_idxs_mapping = {}

    def insert(self, val: int) -> bool:
        if val in self.val_idxs_mapping:
            result = False
        else:
            self.val_idxs_mapping[val] = set()
            result = True

        self.vals.append(val)
        self.val_idxs_mapping[val].add(len(self.vals) - 1)

        return result
        
    def remove(self, val: int) -> bool:
        if val not in self.val_idxs_mapping:
            return False
        
        if self.vals[-1] == val:
            self.val_idxs_mapping[val].remove(len(self.vals) - 1)
            self.vals.pop()
            if len(self.val_idxs_mapping[val]) == 0:
                self.val_idxs_mapping.pop(val)

            return True
        
        val_idx = list(self.val_idxs_mapping[val])[0]
        last_val = self.vals[-1]
        # move last_val to val idx
        self.val_idxs_mapping[last_val].remove(len(self.vals) - 1)
        self.val_idxs_mapping[last_val].add(val_idx)
        self.vals[val_idx] = last_val

        # move val to last_idx and remove
        self.val_idxs_mapping[val].remove(val_idx)
        if len(self.val_idxs_mapping[val]) == 0:
            self.val_idxs_mapping.pop(val)

        self.vals.pop()

        return True
        

    def getRandom(self) -> int:
        idx = int(len(self.vals) * random.random())
        return self.vals[idx]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()