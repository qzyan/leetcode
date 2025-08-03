class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.dummy = Node()
        self.tail = self.dummy
        self.key_prev_node = {}
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.key_prev_node:
            return -1
        node = self.key_prev_node[key].next
        result = node.val
        self.move_to_tail(node)

        return result

    def put(self, key: int, value: int) -> None:
        if key in self.key_prev_node:
            node = self.key_prev_node[key].next
            node.val = value
            self.move_to_tail(node)
            return
        
        if self.size == self.capacity:
            self.remove(self.dummy.next)
            self.size -= 1

        node = Node(key, value)
        self.append(node)
        self.size += 1

    def append(self, node):
        self.tail.next = node
        self.key_prev_node[node.key] = self.tail
        self.tail = node

    def remove(self, node):
        # link the prev_node with the next_node
        prev_node = self.key_prev_node[node.key]
        prev_node.next = node.next
        if node.next:
            self.key_prev_node[node.next.key] = prev_node

        # if remove the tail, move the tail back
        if self.tail == node:
            self.tail = prev_node

        # delete the item in mapping
        self.key_prev_node.pop(node.key)

    def move_to_tail(self, node):
        if node == self.tail:
            return

        self.remove(node)
        self.append(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)