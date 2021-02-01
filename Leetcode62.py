# Constraints:
# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 10^9.

# Approach 1. Bottom-up
# For each row/col, calculate how many ways to reach there
# O(MN), space O(min(M,N))

class Solution(object):
    def uniquePaths(self, m, n):
        m, n = max(m, n), min(m, n)
        arr = [1] * n
        for _ in range(1, m):
            for i in range(0, n):
                if i-1 < 0: continue
                arr[i] += arr[i-1]
            
        return arr[-1]

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([3, 7], 28),
    Test([3, 2], 3),
    Test([7, 3], 28),
    Test([3, 3], 6),
]

solver = Solution()
for test in tests:
    print("{} {}".format(solver.uniquePaths(test.input[0], test.input[1]), test.output))
