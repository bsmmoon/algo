# Approach 1. Brute force
# O(N^2)

# Approach 2.
# Note that product(n) = product(n-1) * arr[n-1] / arr[n]
# This makes computing subsequent element cost O(1) instead of O(N)
# Thus, O(N)
# BUT it can't handle when there is 0!!

# Approach 3.
# 1. compute product of all
# 2. product(n) = product(all) / arr[n]
# Also O(N) and simpler
# BUT it can't handle when there is 0!!

# Observation: if there exists more than one 0s, all are 0
# => we only need to handle case where there is one 0!
# => all elements are 0 except the 0 itself!!!!!!

class Solution(object):
    def productExceptSelf(self, nums):
        product = 1
        zerodex = False
        for i, num in enumerate(nums):
            if num == 0:
                if zerodex is not False: return [0] * len(nums)
                zerodex = i
                continue
            product *= num
            
        if zerodex:
            output = [0] * len(nums)
            output[zerodex] = product
            return output
        
        for i, num in enumerate(nums):
            nums[i] = int(product / num)
        
        return nums

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([1,2,3,4], [24,12,8,6]),
    Test([-1,1,0,-3,3], [0,0,9,0,0]),
    Test([-1,1,0,0,3], [0,0,0,0,0]),
    Test([0,0], [0,0])
]

solver = Solution()
for test in tests:
    output = solver.productExceptSelf(test.input)
    print("{} {}".format(output, test.output))
