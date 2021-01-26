# Constraints:
#
# 0 <= s.length <= 3 * 104
# s[i] is '(', or ')'.
#
# BCR: O(N)

class Solution(object):
    def longestValidParentheses(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if len(stack) > 0 and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)
        
        longest = 0
        prev = len(s)
        while len(stack) > 0:
            index = stack.pop()
            longest = max(longest, prev - index - 1)
            prev = index
        longest = max(longest, prev)
        return longest


class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test("()", 2),
    Test("(()", 2),
    Test(")()())", 4),
    Test(")(())", 4),
    Test("", 0),
    Test("()(()", 2),
    Test("(()(((()", 2),
]

solver = Solution()
for test in tests:
    print(solver.longestValidParentheses(test.input), test.output)
