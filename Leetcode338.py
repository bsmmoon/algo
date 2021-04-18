class Solution(object):
    def countBits(self, target):
        memo = [0] * (target + 1)
        msb = 1
        for num in range(1, target+1):
            if num >= msb * 2: msb *= 2
            memo[num] = 1 + memo[num - msb]
        return memo

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test(2, [0,1,1]),
    Test(5, [0,1,1,2,1,2]),
    Test(8, [0,1,1,2,1,2,2,3,1]),
]

solver = Solution()
for test in tests:
    output = solver.countBits(test.input)
    print("{} {}".format(output, test.output))
        
        
        
