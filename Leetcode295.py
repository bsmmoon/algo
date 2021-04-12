# Constraints:
# -10^5 <= num <= 10^5
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 10^4 calls will be made to addNum and findMedian.
 
# Follow up:
# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

import heapq

class MedianFinder(object):

    def __init__(self):
        self.left, self.right = [], []
        
    def addNum(self, num):
        if not self.right: return self.addToRight(num)
        
        if len(self.left) == len(self.right):
            if self.peekLeft() < num:
                self.addToRight(num)
            else:
                self.addToRight(self.popLeft())
                self.addToLeft(num)

        else:
            if num < self.peekRight():
                self.addToLeft(num)
            else:
                self.addToLeft(self.popRight())
                self.addToRight(num)

    def findMedian(self):
        if len(self.left) < len(self.right): return self.peekRight()
        return (self.peekLeft() + self.peekRight()) / 2.0
        
    def addToLeft(self, num):
        heapq.heappush(self.left, num * -1)
        
    def addToRight(self, num):
        heapq.heappush(self.right, num)
        
    def peekLeft(self):
        return self.left[0] * -1
    
    def peekRight(self):
        return self.right[0]
        
    def popLeft(self):
        return heapq.heappop(self.left) * 1
    
    def popRight(self):
        return heapq.heappop(self.right)

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output
        
tests = [
    Test((
        ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
        [[], [1], [2], [], [3], []]
    ), [None, None, None, 1.5, None, 2.0])
]

for test in tests:
    medianFinder = None
    output = []
    for command, args in zip(*test.input):
        if command == "MedianFinder":
            medianFinder = MedianFinder()
            output.append(None)
        elif command == "addNum":
            medianFinder.addNum(*args)
            output.append(None)
        elif command == "findMedian":
            output.append(medianFinder.findMedian())
    
    print("{}\n{}".format(output, test.output))
