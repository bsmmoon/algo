# Constraints:
# 1 <= n <= 45

class Solution(object):
    def climbStairs(self, n):
        memo = { 0: 1 }
        for i in range(1, n+1):
            memo[i] = memo.get(i - 1, 0) + memo.get(i - 2, 0)
        return memo[n]
    
    def _climbStairs(self, n, memo={}):
        if n < 0: return 0
        if n == 0: return 1
        if memo.get(n): return memo[n]
        memo[n] = self._climbStairs(n-1) + self._climbStairs(n-2)
        return memo[n]

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test(2, 2),
    Test(3, 3),
]

solver = Solution()
for test in tests:
    print(solver.climbStairs(test.input), test.output)
