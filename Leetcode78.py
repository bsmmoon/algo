# Constraints:
#  1 <= nums.length <= 10
#  -10 <= nums[i] <= 10
#  All the numbers of nums are unique.

# BCR: O(2^N) because needs to make all possible subsets

# Approach 1.
# Recurssively visit each element and decide whether to select or not
# O(2^N), space: O(2^N)

class Solution(object):
    def subsets(self, nums):
        result = []
        self.recurr(nums, 0, [], result)
        return result
        
    def recurr(self, nums, index, subset, result):
        if not index < len(nums):
            result.append(subset)
            return
        
        self.recurr(nums, index+1, subset, result)
        self.recurr(nums, index+1, subset + [nums[index]], result)
        
class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
    Test([0], [[],[0]]),
]

solver = Solution()
for test in tests:
    print("{}\n{}".format(solver.subsets(test.input), test.output))

