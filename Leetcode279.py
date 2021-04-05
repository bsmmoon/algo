# Constraints:
# 1 <= n <= 10^4

# Approach 1 Greedy
# starting from n, move down and take the largest square numbers
# does not guarantee correct answer!

# Approach 2 DP
# build up numSquares from 1 to target
# O(N*sqrt(N)), space O(N)

import math

class Solution(object):
    def numSquares(self, target):
        memo = { 0: 0 }
        
        for candidate in range(1, int(math.floor(pow(target, 0.5))) + 1):
            memo[pow(candidate, 2)] = 1
        
        for num in range(target+1):
            if num in memo: continue
        
            for candidate in range(1, int(math.floor(pow(num, 0.5))) + 1):
                prev = num - pow(candidate, 2)
                
                if prev < 0: continue

                if num in memo:
                    memo[num] = min(memo[num], memo[prev] + 1)
                else:
                    memo[num] = memo[prev] + 1
                
        return memo[target]

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test(12, 3),
    Test(13, 2),
    Test(16, 1),
    Test(17, 2),
]

solver = Solution()
for test in tests:
    output = solver.numSquares(test.input)
    print("{} {}".format(output, test.output))
