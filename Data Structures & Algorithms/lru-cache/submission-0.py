class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = None
        self.right = None

    def get(self, key: int) -> int:
        if key in self.cache:
            tmpNext = self.cache[key].next
            tmpPrev = self.cache[key].prev
            if tmpNext:
                tmpNext.prev = tmpPrev
            else:
                self.right = tmpPrev
            if tmpPrev:
                tmpPrev.next = tmpNext
            else:
                self.left = tmpNext

            tmpRight = self.right
            if tmpRight:
                tmpRight.next = self.cache[key]
            else:
                self.left = self.cache[key]
            self.right = self.cache[key]
            self.right.prev = tmpRight
            self.right.next = None

            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            tmpNext = self.cache[key].next
            tmpPrev = self.cache[key].prev
            if tmpNext:
                tmpNext.prev = tmpPrev
            else:
                self.right = tmpPrev
            if tmpPrev:
                tmpPrev.next = tmpNext
            else:
                self.left = tmpNext

        self.cache[key] = Node(key, value)
        tmpRight = self.right
        if tmpRight:
            tmpRight.next = self.cache[key]
        else:
            self.left = self.cache[key]
        self.right = self.cache[key]
        self.right.prev = tmpRight
        self.right.next = None

        if len(self.cache) > self.cap:
            lru = self.left
            tmpNext = lru.next
            if tmpNext:
                tmpNext.prev = None
            else:
                self.right = None
            self.left = tmpNext
            del self.cache[lru.key]