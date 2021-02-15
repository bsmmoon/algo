# In other words.. can you construct s using wordDict?

# JUMP you fool

class Solution(object):
    def wordBreak(self, s, wordDict):
        if not s: return True
        
        memo = set()
        reachable = [0]
        
        while reachable:
            pos = reachable.pop()
            if pos in memo: continue
        
            for word in wordDict:
                jumped = pos + len(word)
                if jumped > len(s): continue
                if s[pos:jumped] != word: continue
                
                if jumped == len(s): return True
                    
                reachable.append(jumped)
            memo.add(pos)
        return False

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test(("leetcode", ["leet", "code"]), True),
    Test(("applepenapple", ["apple", "pen"]), True),
    Test(("catsandog", ["cats", "dog", "sand", "and", "cat"]), False),
    Test(("catsanddog", ["cats", "dog", "sand", "and", "cat"]), True),
    Test(("", ["cats", "dog", "sand", "and", "cat"]), True),
    Test(("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["aa","aaa","ba"]), None)
]

solver = Solution()
for test in tests:
    print("{} {}".format(solver.wordBreak(*test.input), test.output))
