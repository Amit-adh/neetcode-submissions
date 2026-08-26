class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def removeLRU(self):
        node = self.left.next

        next = node.next
        self.left.next = next
        next.prev = self.left

        self.cache.pop(node.key)

    def addRecent(self, node):
        prev = self.right.prev
        
        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache.get(key)

            self.remove(node)
            self.addRecent(node)

            self.cache[key] = node

            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache.get(key)
            node.val = value

            self.remove(node)
            self.addRecent(node)

            return 

        node = Node(key, value)
        self.cache[key] = node
        self.addRecent(node)
        
        if len(self.cache) > self.cap:
            self.removeLRU()
