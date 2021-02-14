# BCR: O(N)

# Approach 1.
# for each num O(N)
#   find its match O(N)
# O(N^2), space: O(1)

# Approach 2.
# for each num O(N)
#   add to a set if it isn't already
#   else remove
# return the remaining value
# O(N), space: O(N)

# Approach 3.
# Since x ^ x = 0,
# if we do ^ on all elements, all duplicates will cancel out eventually
# O(N), space: O(1)

import functools 

class Solution(object):
    def singleNumber(self, nums):
        return functools.reduce(lambda a, b: a ^ b, nums)
        
    def _singleNumber(self, nums):
        single = set()
        for num in nums:
            if num in single:
                single.remove(num)
            else:
                single.add(num)
        return single.pop()

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([2,2,1], 1),
    Test([4,1,2,1,2], 4),
    Test([1], 1),
]

solver = Solution()
for test in tests:
    print("{} {}".format(solver.singleNumber(test.input), test.output))
