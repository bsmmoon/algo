# Constraints:
#  1 <= nums.length <= 3 * 10^4
#  0 <= nums[i] <= 10^5

# Since the value is the "maximum" jump, you can reach anywhere in that "area"
# Use pointers to expand the area until it reaches the end
# Observation: In can fail iff there exists 0!!

class Solution(object):
    def canJump(self, nums):
        if len(nums) == 1: return True
        
        if all(map(lambda x: x != 0, nums)): return True
        
        last = len(nums) - 1
        left, right = 0, 0
        while left <= right:
            next_left = right + 1
            for i in range(left, next_left):
                if right < i + nums[i]:
                    right = i + nums[i]
                    if last <= right: return True
            left = next_left
        
        return False

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([2,3,1,1,4], True),
    Test([3,2,1,0,4], False),
    Test([2,0,0], True),
    #Test([3,0,8,2,0,0,1], True),
    #Test([8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5], True),
    Test([2,0,2,0,1], True),
    Test([0], True)
]

solver = Solution()
for test in tests:
    print("{} {}".format(solver.canJump(test.input), test.output))
