# Constraints:
# 0 <= nums.length <= 300
# -231 <= nums[i] <= 231 - 1

# Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space?

# Let N = nums.length

# Approach 1.
# Sort O(NlogN)
# Iterate and find the first missing positive integer O(N)
# O(NlogN) + O(N) = O(NlogN)
#
# Approach 2.
# Sort O(NlogN)
# Bsearch where positive integer starts O(logN)
# Bsearch index that's out of place O(logN)
# O(NlogN) + O(logN) = O(NlogN)
#
# Approach 3.
# Since nums.length <= 300
# Create an array of size 300. O(1), space: O(N)
# Iterate and set arr[i] = True O(N)
# Iterate and find the first element that's not True O(N)
# O(N), space: O(N)
#
# Approach 4.
# Create an integer
# Iterate and set ith bit to 1 O(N)
# Iterate and find the first element that's not True O(N)
# O(N), space: O(1)

class Solution(object):
    def firstMissingPositive(self, nums):
        bits = 0
        for num in nums:
            if num <= 0 or 300 < num: continue
            bits |= 1 << num
        i = 1
        while True:
            if not bits & (1 << i): return i
            i += 1
        return i

def printBits(bits):
    output = ""
    while bits > 0:
        output += str(bits % 2)
        bits >>= 1
    print(output[::-1])

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([1,2,0], 3),
    Test([3,4,-1,1], 2),
    Test([7,8,9,11,12], 1),
]

solver = Solution()
for test in tests:
    print(solver.firstMissingPositive(test.input), test.output)
