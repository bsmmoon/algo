# Constraints:
# 1 <= capacity <= 3000
# 0 <= key <= 3000
# 0 <= value <= 104
# At most 3 * 104 calls will be made to get and put.

# Follow up: Could you do get and put in O(1) time complexity?

# Approach 1.
# { key => (value, age) }
# get
#   update age of the key to the max + 1
# put
#   if exceeding capacity, find and evict the pair with min age
#   add a new pair with age of max + 1
# complexity rises from finding one with max or min O(N)

# Approach 1.1
# keep oldest and youngest
# each entry keep next and prev
# get
#   connect prev and next
#   append entry to the end
#   O(1)
# push
#   if not in cache
#     set oldest's next as oldest and its prev None
#     del oldest
#     append entry to the end
#   if in cache
#     do same as get plus update value
#   O(1)

class Entry:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
        
    def __repr__(self):
        return "{}, {}".format(self.key, self.value)
        
    def values(self):
        arr = []
        entry = self
        while entry:
            arr.append(entry.value)
            entry = entry.next
        return arr

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = None, None
    
    # O(1)
    def get(self, key):
        entry = self.cache.get(key)
        
        if not entry: return -1
        
        # remove the entry
        self.remove_entry(entry)
        
        # append the entry to the end
        self.append(entry)

        return entry.value

    # O(1)
    def put(self, key, value):
        if key in self.cache:
            self.remove_entry(self.cache.get(key))
        elif self.is_full():
            self.remove_entry(self.head)
        
        # append the entry to the end
        self.append(Entry(key, value))

    def is_full(self):
        return not len(self.cache) < self.capacity
        
    def remove_entry(self, entry):
        if entry.prev and entry.next:
            entry.prev.next = entry.next
            entry.next.prev = entry.prev
        
        if entry == self.head:  # entry is head
            self.head = entry.next
            if self.head: self.head.prev = None
        
        if entry == self.tail:
            self.tail = entry.prev
            if self.tail: self.tail.next = None
            
        del self.cache[entry.key]

    def append(self, entry):
        if self.tail == entry: return
    
        if self.tail:
            self.tail.next = entry
            
        entry.prev, entry.next = self.tail, None
        
        self.tail = entry
        if not self.head: self.head = entry
        
        self.cache[entry.key] = entry

# Your LRUCache object will be instantiated and called as such:

class Test:
    def __init__(self, commands, args, output):
        self.lines = zip(commands, args)
        self.output = output
        self.obj = None
        
    def run(self):
        output = []
        for command, args in self.lines:
            if command == "LRUCache":
                self.obj = LRUCache(*args)
                output.append(None)
            elif command == "get":
                output.append(self.obj.get(*args))
            elif command == "put":
                self.obj.put(*args)
                output.append(None)
            # print("{} {}\n\t{}".format(command, args, self.obj.head.values() if self.obj.head else None))
        return output

tests = [
    Test(
        ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
        [None, None, None, 1, None, -1, None, -1, 3, 4]
    ),
    Test(
        ["LRUCache", "put", "get", "get"],
        [[2], [1, 1], [1], [2]],
        [None, None, 1, -1]
    ),
    Test(
        ["LRUCache", "put", "put", "put", "get", "get", "get"],
        [[2], [1, 1], [2, 2], [3, 3], [1], [2], [3]],
        [None, None, None, None, -1, 2, 3]
    ),
    Test(
        ["LRUCache", "put", "put", "get", "put", "get", "get", "get"],
        [[2], [1, 1], [2, 2], [1], [3, 3], [1], [2], [3]],
        [None, None, None, 1, None, 1, -1, 3]
    ),
    Test(
        ["LRUCache", "put", "put", "put", "put", "get", "get", "get"],
        [[2], [1, 1], [2, 2], [1, 11], [3, 3], [1], [2], [3]],
        [None, None, None, None, None, 11, -1, 3]
    ),
    Test(
        ["LRUCache", "put", "get", "put", "put", "get", "get"],
        [[1], [1, 1], [1], [2, 2], [3, 3], [2], [3]],
        [None, None, 1, None, None, -1, 3]
    )
]

for test in tests:
    output = test.run()
    print("{}\n{}".format(output if output else None, test.output))
