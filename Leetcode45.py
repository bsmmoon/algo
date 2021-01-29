# Constraints:
# 1 <= nums.length <= 3 * 10^4
# 0 <= nums[i] <= 10^5

# [2,3,1,1,4]
# 0->1->2->3->4
# 0->1->"3"
# 0->1->4
# 0->"2"

# Approach 1.
# Try all the possible ways
#
# Approach 2.
# Memoise "completed" position
#
# Approach 3. Bottom up
# Count jump from the beginning, greedily selecting the largest jump
# Update minimum value when a sequence of jumps finish
# Anything that exceed that minimum value can return immediately
# "How many jumps did it take to get here? Should I go further?"

# Approach 4. Expansion??
# From "left", find the furthest you can go in one step.
# Set that one as the new "left" and continue until the end is inside the region
# https://leetcode.com/problems/jump-game-ii/discuss/170518/8-Lines-in-Python!-Easiest-Solution!

class Solution(object):
    def jump(self, nums):
        if len(nums) <= 1: return 0
        
        left, right = 0, nums[0]
        count = 1
        while right < len(nums) - 1:
            count += 1
            nxt = max(i + nums[i] for i in range(left, right + 1))
            left, right = right, nxt
        return count

    def _jump(self, nums):
        memo = [100000] * len(nums)
        self.recurr(nums, memo, 0, 0)
        return memo[-1]
        
    def recurr(self, nums, memo, index, count):
        if not index < len(nums): return
        
        if memo[index] <= count: return
        
        memo[index] = count
        
        if index == len(nums) - 1: return
        
        for i in range(1, nums[index] + 1)[::-1]:
            self.recurr(nums, memo, index+i, count+1)
            
class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([2,3,1,1,4], 2),
    Test([2,3,0,1,4], 2),
    Test([1,2], 1),
    Test([2,1], 1),
]

solver = Solution()
for test in tests:
    print(solver.jump(test.input), test.output)
