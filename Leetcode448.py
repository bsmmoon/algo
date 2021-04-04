# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

class Solution(object):
    def findDisappearedNumbers(self, nums):
        for num in nums:
            while nums[num-1] != num:
                nums[num-1], num = num, nums[num-1]
        
        return [i+1 for i in range(len(nums)) if nums[i] != i+1]

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([4,3,2,7,8,2,3,1], [5,6]),
    Test([1,1], [2]),
]

solver = Solution()
for test in tests:
    output = solver.findDisappearedNumbers(test.input)
    print("{} {}".format(output, test.output))

