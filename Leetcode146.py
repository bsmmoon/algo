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
    def __init__(self, value, age, prev=None, next=None):
        self.value = value
        self.age = age
        self.prev = prev
        self.next = next

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.nextAge = 0

    # O(1)
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        entry = self.cache.get(key)
        if not entry: return -1
        
        entry.age = self.nextAge
        self.nextAge += 1
        return entry.value

    # O(N)
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.cache and not len(self.cache) < self.capacity:
            self.evict()
        self.cache[key] = Entry(value, self.nextAge)
        self.nextAge += 1
        
    # O(N)
    def evict(self):
        minAge = self.minAge()
        for key in self.cache:
            if self.cache[key].age == minAge:
                del self.cache[key]
                return
            
    # O(N)
    def minAge(self):
        if not self.cache: return 0
        return min(self.cache.values(), key=lambda x: x.age).age

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
            # print("{} {}\n\t{}".format(command, args, self.obj.cache))
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
]

for test in tests:
    output = test.run()
    print("{}\n{}".format(output if output else None, test.output))
