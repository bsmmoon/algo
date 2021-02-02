# Constraints:
#  m == grid.length
#  n == grid[i].length
#  1 <= m, n <= 200
#  0 <= grid[i][j] <= 100

# Approach 0. Recurssive
# Recurssively visit every possible paths and find the minimum path sum
# The length of path will be M + N - 1, and most of them will have 2 choices to make.
# O(2^(M+N))

# Approach 1. Bottom-up
# Create m x n array for path sum
# For each row - O(M)
#  For each col - O(N)
#   set its path sum as min(known path sum, left + top)  - O(1)
# Return the value at the end
# O(MN), space: O(MN)

# Approach 1.1 enhanced
# Use 1 x n array instead
# O(MN), space: O(N)

class Solution(object):
    def minPathSum(self, grid):
        path_sums = [] + grid[0]
        for col, val in enumerate(path_sums):
            if col == 0: continue
            path_sums[col] += path_sums[col-1]
        
        for vals in grid[1:]:
            for col, val in enumerate(vals):
                path_sums[col] = min(
                    path_sums[col],
                    path_sums[col-1] if col > 0 else 1000000
                ) + val

        return path_sums[-1]
        
class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([[1,3,1],[1,5,1],[4,2,1]], 7),
    Test([[1,2,3],[4,5,6]], 12),
]

solver = Solution()
for test in tests:
    print("{} {}".format(solver.minPathSum(test.input), test.output))
