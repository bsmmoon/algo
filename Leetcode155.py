# Constraints
# Methods pop, top and getMin operations will always be called on non-empty stacks.

# Approach 1.
# Use array for stack
# Use heap to find min value
# push O(log n)
# pop O(n log n)
# top O(1)
# getMin O(1)

# Approach 2.
# Since we are only removing top,
# we just need to know the min up to each level

class MinStack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append((x, min(x, self.stack[-1][1]) if self.stack else x))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]


import heapq

class _MinStack(object):
    def __init__(self):
        self.stack = []
        self.heap = []

    def push(self, x):
        self.stack.append(x)
        heapq.heappush(self.heap, x)

    def pop(self):
        self.stack.pop()
        self.heap = [] + self.stack
        heapq.heapify(self.heap)

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.heap[0]

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([
        ["MinStack","push","push","push","getMin","pop","top","getMin"],
        [[],[-2],[0],[-3],[],[],[],[]]
    ], [None,None,None,None,-3,None,0,-2]),
    Test([
        ["MinStack","push","push","push","getMin","top","pop","getMin"],
        [[],[-2],[0],[-1],[],[],[],[]]
    ], [None,None,None,None,-2,-1,None,-2]),
    Test([
        ["MinStack","push","top","push","top"],
        [[],[1],[],[2],[]]
    ], [None,None,1,None,2]),
    Test([
        ["MinStack","push","push","top","pop","top"],
        [[],[1],[2],[],[],[]]
    ], [None,None,None,2,None,1]),
    Test([
        ["MinStack","push","getMin","push","getMin"],
        [[],[1],[],[2],[]]
    ], [None,None,1,None,1]),
    Test([
        ["MinStack","push","push","getMin","pop","getMin"],
        [[],[2],[1],[],[],[]]
    ], [None,None,None,1,None,2]),
]

for test in tests:
    output = []
    stack = None
    for command, args in list(zip(*test.input)):
        if command == "MinStack":
            stack = MinStack()
            output.append(None)
        elif command == "push":
            output.append(stack.push(*args))
        elif command == "pop":
            output.append(stack.pop(*args))
        elif command == "top":
            output.append(stack.top(*args))
        elif command == "getMin":
            output.append(stack.getMin(*args))
    print("{}\n{}".format(output, test.output))
