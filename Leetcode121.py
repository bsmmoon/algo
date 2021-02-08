# Constraints:
#  1 <= prices.length <= 10^5
#  0 <= prices[i] <= 10^4

# Approach 0: Brute
#  for each day O(N)
#   for each of the rest of the days O(N)
#    find max profit
# O(N^2)

# Observation: What's max price for i is also max price for i-1, i-2, etc...

# Approach 1. Move backward
#  for each day in reverse order, O(N)
#   update max selling price
#   update max profit
# O(N)

class Solution(object):
    def maxProfit(self, prices):
        profit, selling_price = 0, 0
        for price in prices[::-1]:
            if selling_price < price:
                selling_price = price
                continue
            profit = max(profit, selling_price - price)
        return profit
        
class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([7,1,5,3,6,4], 5),
    Test([7,6,4,3,1], 0),
]

solver = Solution()
for test in tests:
    print("{} {}".format(solver.maxProfit(test.input), test.output))

