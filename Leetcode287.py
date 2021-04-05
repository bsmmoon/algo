# Constraints:
# 2 <= n <= 3 * 10^4
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.

# Follow up:
# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem without modifying the array nums?
# Can you solve the problem using only constant, O(1) extra space?
# Can you solve the problem with runtime complexity less than O(n^2)?

import collections

class Solution(object):
    def findDuplicate(self, nums):
        for i, num in enumerate(nums):
            while i+1 != num:
                if num == nums[num-1]: return num
                nums[num-1], num = num, nums[num-1]
                nums[i] = num
    
    def ___findDuplicate(self, nums):
        visited = set()
        for num in nums:
            if num in visited: return num
            visited.add(num)
    
    def __findDuplicate(self, nums):
        return collections.Counter(nums).most_common(1)[0][0]
    
    def _findDuplicate(self, nums):
        nums.sort()
        prev = nums[0]
        for num in nums[1:]:
            if prev == num: return num
            prev = num

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([1,3,4,2,2], 2),
    Test([3,1,2,4,3], 3),
    Test([1,1], 1),
    Test([1,1,2], 1),
    Test([7,9,7,4,2,8,7,7,1,5], 7)
]

solver = Solution()
for test in tests:
    output = solver.findDuplicate(test.input)
    print("{} {}".format(output, test.output))
