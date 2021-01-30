# Constraints:
# matrix.length == n
# matrix[i].length == n
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

# Observation:
# Each "layer" is an independent problem themselves
# Each set of four points on all sides is an independent problem themselves

from math import ceil

class Solution(object):
    def rotate(self, matrix):
        for r in range(0, int(ceil(len(matrix) / 2))):
            self.rotateLayer(matrix, r)
        return matrix
        
    def rotateLayer(self, matrix, r):
        for c in range(r, len(matrix)-r-1):
            self.rotatePoints(matrix, r, c)

    def rotatePoints(self, matrix, r, c):
        width = len(matrix)
        temp = matrix[r][c]
        matrix[r][c] = matrix[width-c-1][r]
        matrix[width-c-1][r] = matrix[width-r-1][width-c-1]
        matrix[width-r-1][width-c-1] = matrix[c][width-r-1]
        matrix[c][width-r-1] = temp
                
class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]),
    Test([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]], [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]),
    Test([[1]], [[1]]),
    Test([[1,2],[3,4]], [[3,1],[4,2]]),
]

solver = Solution()
for test in tests:
    print("{}\n{}".format(solver.rotate(test.input), test.output))
