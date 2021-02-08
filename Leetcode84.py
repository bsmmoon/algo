# Constraints:
#  1 <= heights.length <= 105
#  0 <= heights[i] <= 104

# Let N = heights.length, H = heights[i]

# Approach 1
# for each possible height O(H)
#   find sequence of heights that's geq and calculate O(N)
# O(NH), space: O(1)

# Approach 2.
# for each height O(N)
#   if less than previous, pop all geq and calculate max area
#   push to queue
# O(N), space: O(N)

class Solution(object):
    def largestRectangleArea(self, heights):
        max_area = 0
        stack = []
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                j, h = stack.pop()
                max_area = max(max_area, h * (i - j))
                start = j
            stack.append((start, height))

        for j, h in stack:
            max_area = max(max_area, h * (len(heights) - j))
        return max_area
                
class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([2,1,5,6,2,3], 10),
    Test([2,4], 4),
    Test([2,1,2], 3),
]

solver = Solution()
for test in tests:
    print("{} {}".format(solver.largestRectangleArea(test.input), test.output))

