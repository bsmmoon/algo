# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

# Ideas:
# when visiting an island, we probably wanna visit all its lands.
# we also wanna make sure not to visit the same island again.

# Approach 1.
# when 1,
#   visit its adjacent lands that's 1
#   set all visited 0
# O(MN)

class Solution(object):
    def numIslands(self, grid):
        count = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == "0": continue
                count += 1
                self.visit(grid, r, c)
        return count
        
    def visit(self, grid, r, c):
        if not (0 <= r < len(grid)): return
        if not (0 <= c < len(grid[r])): return
        if grid[r][c] == "0": return
    
        grid[r][c] = "0"
        self.visit(grid, r, c-1)
        self.visit(grid, r, c+1)
        self.visit(grid, r-1, c)
        self.visit(grid, r+1, c)
        
class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ], 1),
    Test([
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ], 3),
    Test([
      ["1","1","1"],
      ["0","1","0"],
      ["1","1","1"]
     ], 1),
]

solver = Solution()
for test in tests:
    output = solver.numIslands(test.input)
    print("{} {}".format(output, test.output))
