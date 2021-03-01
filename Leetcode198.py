# Constraints:
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 400

# BCR: O(N)

# Approach 1. top down
# if index 0 is taken, the ensuing subproblem is one that starts at index 2
# recurssively travel following the above
# store best value starting at index i on a memo table
# O(N), space: O(N)

# Approach 2. bottom up
# construct the memo from index i by setting it as memo[i-2] + value
# O(N), space: O(N)

# Approach 3. bottom up enhanced
# since only up to memo[i-2] is being used, only i-2 and i-1 needs to be stored
# O(N), space: O(1)

class Solution(object):
    def rob(self, nums):
        prepre, pre = 0, 0
        for num in nums: prepre, pre = max(prepre, pre), prepre + num
        return max(prepre, pre)
        
class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([1,2,3,1], 4),
    Test([2,7,9,3,1], 12),
    Test([], 0),
    Test([1], 1),
    Test([1,2], 2),
    Test([1,2,2], 3),
    Test([1,4,2], 4),
    Test([2,1,1,2], 4),
]

solver = Solution()
for test in tests:
    output = solver.rob(test.input)
    print("{} {}".format(output, test.output))
