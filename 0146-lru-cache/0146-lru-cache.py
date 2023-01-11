class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        # {key: [val, prev_node]} 
        self.key_val_prev_map = {}
        self.dummy = ListNode(-1)
        self.tail = self.dummy
        

    def get(self, key: int) -> int:
        # if not in key_val_prev_map, return -1
        if key not in self.key_val_prev_map:
            return -1
        
        val = self.key_val_prev_map[key][0]
        
        self.delete(key)
        self.add_to_tail(key, val)
        
        return val
        # delete the node from the linked list
        # add the node to the end of the linkedlist
        # return the key_val_prev_map[key][0]

    def put(self, key: int, value: int) -> None:
        if key in self.key_val_prev_map:
            self.delete(key)
            self.add_to_tail(key, value)
            return
        
        if self.size == self.capacity:
            key_to_delete = self.dummy.next.key
            self.delete(key_to_delete)
            self.add_to_tail(key, value)
            return
        
        self.size += 1
        self.add_to_tail(key, value)
        
        # if key exists in the key_val_prev_map
            # delete the node from the linked list
            # add the node to the end of the linkedlist
            # update the key_val_prev_map[key][0]
        # if key is new
            # if reached the capacity:
                # delete the first node of the linked list
                # delete the key_val from the key_val_prev_map
            
            # add the new node to the end of the linkedlist
            # add the key-val pair to the hashmap

    def delete(self, key):
        # delete the node from the linkedlist
        prev_node = self.key_val_prev_map[key][1]
        curr_node = prev_node.next
        next_node = curr_node.next
        
        curr_node.next = None
        prev_node.next = next_node
        
        if next_node:
            self.key_val_prev_map[next_node.key][1] = prev_node
        else:
            self.tail = prev_node
        
        # delete the key from hashmap
        self.key_val_prev_map.pop(key)

    
    def add_to_tail(self, key, val):
        # add the node to the tail
        # add the key: (val, prev_node) to the hashmap
        node = ListNode(key)
        self.tail.next = node
        prev_node = self.tail
        self.tail = node
        
        self.key_val_prev_map[key] = [val, prev_node]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)