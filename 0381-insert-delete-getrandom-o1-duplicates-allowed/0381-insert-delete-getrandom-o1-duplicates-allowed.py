import random
class RandomizedCollection:

    def __init__(self):
        self.vals = []
        self.val_indexes_mapping = {}
        
    def insert(self, val: int) -> bool:
        self.vals.append(val)
        index = len(self.vals) - 1
        
        if val in self.val_indexes_mapping:
            self.val_indexes_mapping[val].add(index)
        else:
            self.val_indexes_mapping[val] = {index}
            
        return len(self.val_indexes_mapping[val]) == 1
        
    def remove(self, val: int) -> bool:
        val_indexes = self.val_indexes_mapping.get(val)
        # val never appeared or all val have been removed
        if not val_indexes or len(val_indexes) == 0:
            return False
        
        index_to_update = self.val_indexes_mapping[val].pop()
        last_index = len(self.vals) - 1
        last_val = self.vals[last_index]
        
        # update the todelete ele to last_val
        self.vals[index_to_update] = last_val
        self.val_indexes_mapping[last_val].add(index_to_update)
        
        # delete the last ele in list
        self.val_indexes_mapping[last_val].discard(last_index)
        self.vals.pop()
        
        return True
            

    def getRandom(self) -> int:
        size = len(self.vals)
        index = random.randint(0, size - 1)
        return self.vals[index]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()