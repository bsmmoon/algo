# Constraints:
#  m == board.length
#  n = board[i].length
#  1 <= m, n <= 200
#  1 <= word.length <= 10^3
#  board and word consists only of lowercase and uppercase English letters.

# Let W = wrod.length

# Approach 1. DFS
# For each node O(MN)
#   if sequences match, visit its neighbours O(3^W)
# !! make sure to mark visited
# O((3^W)MN), space: O(MN)

class Solution(object):
    def exist(self, board, word):
        if not self.possible(board, word): return False
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.has_sequence(board, i, j, set(), word, 0): return True
        return False
    
    def possible(self, board, word):
        freq = {}
        for c in word:
            freq[c] = freq.get(c, 0) + 1
        
        for row in board:
            for c in row:
                if c not in freq: continue
                freq[c] -= 1

        for v in freq.values():
            if v > 0: return False
        
        return True
    
    def has_sequence(self, board, i, j, visited, word, index):
        if (i, j) in visited: return False
        if not index < len(word): return True
        if not (0 <= i < len(board)) or not (0 <= j < len(board[i])): return False
        if word[index] != board[i][j]: return False
        
        visited.add((i, j))
        
        if self.has_sequence(board, i, j-1, visited, word, index+1) or\
            self.has_sequence(board, i, j+1, visited, word, index+1) or\
            self.has_sequence(board, i-1, j, visited, word, index+1) or\
            self.has_sequence(board, i+1, j, visited, word, index+1):
            return True
        
        visited.remove((i, j))
        return False
        
        
                
class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([[["A", "B"], ["C", "D"]], "ACDB"], True),
    Test([[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"], True),
    Test([[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"], True),
    Test([[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"], False),
    Test([[["A","A","A","A"],["A","A","A","A"],["A","A","A","B"]], "AAAAAAAAAB"], True),
    Test([[["A","A","A","A"],["A","A","A","A"],["A","A","A","B"]], "AAAC"], False),
    Test([[["C","A","A","A"],["A","A","A","A"],["A","A","A","A"]], "AAAC"], True),
    Test([[["A"]], "A"], True),
    Test([[["A"]], "B"], False),
]

solver = Solution()
for test in tests:
    print("{} {}".format(solver.exist(test.input[0], test.input[1]), test.output))

