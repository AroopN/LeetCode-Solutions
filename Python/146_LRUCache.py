class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.front = None
        self.rear = None
        self.ref = dict()
        self.n = 0
        self.capacity = capacity

    def makeRear(self, node):
        node.prev = self.rear
        self.rear.next = node
        self.rear = node

    def get(self, key: int) -> int:
        if key in self.ref:
            curr = self.ref[key]
            if curr == self.rear:
                return curr.val
            if curr == self.front:
                self.front = curr.next
            else:
                curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.makeRear(curr)
            return curr.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.ref:
            self.ref[key].val = value
            curr = self.ref[key]
            if curr == self.rear:
                return
            if curr == self.front:
                self.front = self.front.next
            else:
                curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.makeRear(curr)
            return

        if self.n < self.capacity:
            self.n += 1
            node = Node(key, value)
            if self.front == None:
                self.rear = node
                self.front = node
                self.ref[key] = node
            else:
                self.makeRear(node)
                self.ref[key] = node
        else:
            self.ref.pop(self.front.key)
            self.front = self.front.next
            node = Node(key, value)
            if not self.front:
                self.rear = node
                self.front = node
                self.ref[key] = node
            else:
                self.makeRear(node)
                self.ref[key] = node
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
