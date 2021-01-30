# Constraints:
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lower-case English letters.

# for each, insert the str into its anagram group O(N)
# how to know which anagram group does it belongst to?
# 26 long frequency tuple
# but since we need it just for id, we can hashify

class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        for string in strs:
            group_id = self.group_id(string)
            groups[group_id] = groups.get(group_id, []) + [string]
        return groups.values()
    
    def group_id(self, string):
        frequencies = [0] * 26
        for c in string:
            frequencies[ord(c) - ord("a")] += 1
        return hash(tuple(frequencies))

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test(["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
    Test([""], [[""]]),
    Test(["a"], [["a"]]),
]

solver = Solution()
for test in tests:
    print("{}\n{}".format(solver.groupAnagrams(test.input), test.output))
