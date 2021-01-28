# Constraints:
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.
# 1 <= target <= 500
# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# N = candidates.length
# T = target
#
# Approach 1 Brute force all the way
# While sum < target, try adding every candidates
# O(N^T).. very broadly speaking, since the worst we can do is T number of 1s
#
# Approach 2.1 Bottom Up
# For T=0, [[]]
# For T=1, [[1] x memo[0]] = [[1]]
# For T=2, [[1] x memo[1], [2] x memo[0]] = [[1,1], [2]]
# For T=3, [[1] x memo[2], [2] x memo[1], [3] x memo[0]] = [[1,1,1], [1,2], [2,1], [3]]
# (needs deduplication)
# ...
# where x denotes combination.
#
# Approach 2.2 Top Down
# ...

class Solution(object):
    def combinationSum(self, candidates, target):
        # return self.recurr(candidates, target, { 0: [[]] })

        memo = { 0: [[]] }
        for i in range(1, target+1):
            memo[i] = set()
            
            for candidate in candidates:
                wanted = i - candidate
                if wanted < 0 or not memo.get(wanted): continue
                
                if wanted == 0:
                    memo[i].add(tuple([candidate]))
                    continue
                
                for combination in memo[wanted]:
                    memo[i].add(tuple(sorted(tuple([candidate]) + combination)))

        return memo[target]
                    
    def top_down(self, candidates, target, memo):
        if target < 0: return ()
        if memo.get(target): return memo[target]
        
        result = set()
        for candidate in candidates:
            wanted = target - candidate
            if wanted == 0:
                result.add(tuple([candidate]))
                continue
            
            for combination in self.recurr(candidates, wanted, memo):
                result.add(tuple(sorted(tuple([candidate]) + combination)))
        memo[target] = result
        return result

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([[2,3,6,7], 7], [[2,2,3],[7]]),
    Test([[2,3,5], 8], [[2,2,2,2],[2,3,3],[3,5]]),
    Test([[2], 1], []),
    Test([[1], 1], [[1]]),
    Test([[1], 2], [[1,1]]),
]

solver = Solution()
for test in tests:
    print(solver.combinationSum(test.input[0], test.input[1]), test.output)
