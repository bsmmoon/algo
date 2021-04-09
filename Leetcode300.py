# Constraints:
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4

# BCR: O(N)

# Observation
# It is NOT always better to take an eligible element than not

# Approach 1.
# Store progresses as num -> length in dictionary

class Solution(object):
    def lengthOfLIS(self, nums):
        progresses = {}
        for num in nums:
            new_progresses = {}
            for last_num, length in progresses.items():
                if last_num < num:
                    new_progresses[num] = max(new_progresses.get(num, 0), length + 1)
                new_progresses[last_num] = max(new_progresses.get(last_num, 0), length)
            new_progresses[num] = max(new_progresses.get(num, 0), 1)
            progresses = new_progresses
        return max(progresses.values())

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([10,9,2,5,3,7,101,18], 4),
    Test([0,1,0,3,2,3], 4),
    Test([7,7,7,7,7,7,7], 1),
    Test([9,10,2], 2),
    Test([9,10,2,3,4], 3),
    Test([9,10,100,1,2,3,4], 4),
    Test([1], 1),
]

solver = Solution()
for test in tests:
    output = solver.lengthOfLIS(test.input)
    print("{} {}".format(output, test.output))
