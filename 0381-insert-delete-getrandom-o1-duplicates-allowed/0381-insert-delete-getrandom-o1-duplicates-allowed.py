import random
class RandomizedCollection:

    def __init__(self):
        self.vals = []
        self.val_indexes_mapping = {}
        
    def insert(self, val: int) -> bool:
        self.vals.append(val)
        index = len(self.vals) - 1
        
        if val in self.val_indexes_mapping:
            already_exists = True
            self.val_indexes_mapping[val].add(index)
        else:
            already_exists = False
            self.val_indexes_mapping[val] = {index}
            
        return not already_exists
        
    def remove(self, val: int) -> bool:
        if val not in self.val_indexes_mapping:
            return False
        
        index_to_update = self.val_indexes_mapping[val].pop()
        last_index = len(self.vals) - 1
        last_val = self.vals[last_index]
        
        if len(self.val_indexes_mapping[val]) == 0:
            self.val_indexes_mapping.pop(val)
        
        if index_to_update != last_index:
            self.vals[index_to_update] = last_val
            
            self.val_indexes_mapping[last_val].discard(last_index)
            self.val_indexes_mapping[last_val].add(index_to_update)
        
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