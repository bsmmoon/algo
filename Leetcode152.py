# Constraints
# The number of nodes in the list is in the range [0, 5 * 10^4].
# -10^5 <= Node.val <= 10^5

# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

# Approach 1
# Find the max positive product and min negative product at each index

class Solution(object):
    def maxProduct(self, nums):
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        result = pow(10, 5) * -1
        
        positive = negative = None
        for num in nums:
            positive_product = positive * num if positive else num
            negative_product = negative * num if negative else num
            positive = max(num, positive_product, negative_product)
            negative = min(num, positive_product, negative_product)
            result = max(result, positive)

        return result
        
        
class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([2,3,-2,4], 6),
    # [2, 2], [6, 6], [-2, -12], [4, -48]
    Test([2,3,-2,4,-1], 48),
    Test([-2,0,-1], 0),
    # [-2, -2], [0, 0], [0, -1]
    Test([-1,-2,0,-1], 2),
    Test([1], 1),
    Test([-2], -2),
    Test([], 0),
]



solver = Solution()
for test in tests:
    output = solver.maxProduct(test.input)
    print("{} {}".format(output, test.output))
