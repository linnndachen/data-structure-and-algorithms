class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        # reference to new entry
        self.nxt = None


class HashTable:
    def __init__(self):
        self.slots = 10
        # current size - resize when half of the table is filled
        self.size = 0
        self.bucket = [None for i in range(self.size)]
        self.threshold = 0.6

    # the hash function. Using one understore at the begining
    # to indicate this is only to use internally
    def _hash(self, key):
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        # returns the slot of the slot of a hash table
        return hv % self.size

    def resize(self):
        new_slots = self.slots * 2
        new_bucket = [None] * new_slots

        for i in range(0, len(self.bucket)):
            head = self.bucket[i]
            while head is not None:
                new_index = self._hash(head.key)
                if new_bucket[new_index] is None:
                    new_bucket[new_index] = HashItem(head.key, head.value)
                else:
                    node = new_bucket[new_index]
                    while node is not None:
                        if node.key is head.key:
                            node.value = head.value
                            node = None
                        elif node.nxt is None:
                            node.nxt = HashItem(head.key, head.value)
                            node = None
                        else:
                            node = node.next
                head = head.next
        self.bucket = new_bucket
        self.slots = new_slots

    def put(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)
        # when the slot is not empty aks facing collision
        while self.bucket[h] is not None:
            if self.bucket[h].key is key:
                break
            h = (h+1) % self.size
        if self.bucket[h] is None:
            self.size += 1
            self.bucket[h] = item

    def get(self, key):
        h = self._hash(key)
        while self.bucket[h] is not None:
            if self.bucket[h].key is key:
                return self.bucket[h].value
            h = (h+1) % self.size
        return None

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)


ht = HashTable()
ht["good"] = "eggs"
ht["better"] = "ham"
ht["best"] = "spam"
ht["ad"] = "do not"
ht["ga"] = "collide"

for key in ("good", "better", "best", "worst", "ad", "ga"):
    v = ht[key]
    print(v)

print("The number of elements is: {}".format(ht.count))
