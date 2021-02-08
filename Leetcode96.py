# Constraints:
#  1 <= n <= 19

# Given root, its left and right subtree becomes their own problem

class Solution(object):
    def numTrees(self, n):
        memo = { 0: 0, 1: 1 }
        
        for i in range(n+1)[2:]:
            memo[i] = 0
            for j in range(i):
                memo[i] += max(1, memo[j]) * max(1, memo[i-j-1])
                
        return memo[n]

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test(1, 1),
    Test(2, 2),
    Test(3, 5),
    Test(4, 14),
    Test(5, 42),
]

solver = Solution()
for test in tests:
    print("{} {}".format(solver.numTrees(test.input), test.output))

