# Constraints:
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

# Let N = nums.length

# BCR: O(N!), space O(N!) since nPn = n!

# Approach 1
# Recurssively select an element out of ramainders
# O(N!), space O(N!) + O(N) where O(N) is for the depth of recurssion

class Solution(object):
    def permute(self, nums):
        self.perms = []
        self.recurr(nums, [])
        return self.perms
        
    def recurr(self, nums, perm):
        if len(nums) == 0:
            self.perms.append(perm)
            return
        
        for i, num in enumerate(nums):
            self.recurr(nums[:i] + nums[i+1:], perm + [num])
        
class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
    Test([0,1], [[0,1],[1,0]]),
    Test([1], [[1]]),
]

solver = Solution()
for test in tests:
    print("{}\n{}".format(solver.permute(test.input), test.output))
