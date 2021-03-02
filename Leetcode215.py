# BCR: O(N)

# Approach 1.
# sort O(NlogN)
# return kth element O(1)
# O(NlogN)

class Solution(object):
    def findKthLargest(self, nums, k):
        return sorted(nums, reverse=True)[k-1]

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test(([3,2,1,5,6,4], 2), 5),
    Test(([3,2,3,1,2,4,5,5,6], 4), 4),
]

solver = Solution()
for test in tests:
    output = solver.findKthLargest(*test.input)
    print("{} {}".format(output, test.output))
