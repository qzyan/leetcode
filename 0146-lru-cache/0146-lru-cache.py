import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.ordered_key_val_dict = collections.OrderedDict()
        self.size = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.ordered_key_val_dict:
            return -1
        
        val = self.ordered_key_val_dict[key]
        self.ordered_key_val_dict.move_to_end(key)
        
        return val

    def put(self, key: int, value: int) -> None:
        if key not in self.ordered_key_val_dict:
            self.ordered_key_val_dict[key] = value
            self.size += 1
        else:
            self.ordered_key_val_dict[key] = value
            self.ordered_key_val_dict.move_to_end(key)
        
        if self.size > self.capacity:
            self.ordered_key_val_dict.popitem(last=False)
            self.size -= 1
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)