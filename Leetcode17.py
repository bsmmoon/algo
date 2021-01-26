# Constraints:
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
#
# BCR: O(3^N) where N = digits.length
# 
# Approach 1.
# Recursion on each digits. Max depth = N
# O(3^N), space: O(3^N + N) = O(3^N)
#
# Approach 2.
# For each digit, insert chars to all existing strings
# O(3^N), space: O(3^N)

class Solution(object):
    def letterCombinations(self, digits):
        if len(digits) == 0: return []
        
        mapping = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"],
        }
        combinations = mapping[digits[0]]
        for digit in digits[1:]:
            appended = []
            for combination in combinations:
                for char in mapping[digit]:
                    appended.append(combination + char)
            combinations = appended
        return combinations

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
    Test("", []),
    Test("2", ["a","b","c"])
]

solver = Solution()
for test in tests:
    print(solver.letterCombinations(test.input), test.output)
