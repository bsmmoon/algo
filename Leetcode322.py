# Constraints:
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4

# Approach 1. Greedy solution
# Use the highest possible denomination as much as possible
# + memo
# O(A), space: O(A), where A=amount
# correctness not guaranteed!

# Approach 2. just dp
# O(A), space: O(A), where A=amount

class Solution(object):
    def coinChange(self, coins, amount):
        memo = [0] + [float("inf")] * amount
        for i in range(1, amount + 1):
            memo[i] = min(memo[i - coin] if i - coin >= 0 else float("inf") for coin in coins) + 1
        return -1 if memo[amount] == float("inf") else memo[amount]

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([[1,2,5], 11], 3),
    Test([[2], 3], -1),
    Test([[1], 0], 0),
    Test([[1], 1], 1),
    Test([[1], 2], 2),
    Test([[186,419,83,408], 6249], 20),
    Test([[342,268,284,65,217,461,245,249,106], 9278], 22),
    Test([[19,28,176,112,30,260,491,128,70,137,253], 8539], 21)
]

solver = Solution()
for test in tests:
    output = solver.coinChange(*test.input)
    print("{} {}".format(output, test.output))
        
        
        
