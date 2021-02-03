# Approach 1.
# Wagner-Fischer algorithm with grid

# Approach 2.
# with just row

class Solution(object):
    def minDistance(self, word1, word2):
        row = list(range(len(word2) + 1))
        
        for i in range(len(word1) + 1)[1:]:
            new_row = [i] + [None] * len(word2)
            for j in range(len(word2) + 1)[1:]:
                substituion_cost = 0 if word1[i-1] == word2[j-1] else 1
                new_row[j] = min(
                    row[j] + 1,
                    new_row[j-1] + 1,
                    row[j-1] + substituion_cost
                )
            row = new_row
        return row[-1]

    def _minDistance(self, word1, word2):
        grid = [list(range(len(word2) + 1))]
        
        for i in range(len(word1) + 1)[1:]:
            grid.append([i] + [None] * len(word2))
        
        for i in range(len(word1) + 1)[1:]:
            for j in range(len(word2) + 1)[1:]:
                substituion_cost = 0 if word1[i-1] == word2[j-1] else 1
                grid[i][j] = min(
                    grid[i-1][j] + 1,
                    grid[i][j-1] + 1,
                    grid[i-1][j-1] + substituion_cost
                )
        return grid[-1][-1]

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test(["horse", "ros"], 3),
    Test(["intention", "execution"], 5,)
]

solver = Solution()
for test in tests:
    print("{} {}".format(solver.minDistance(test.input[0], test.input[1]), test.output))
