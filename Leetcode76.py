# Constraints:
#  1 <= s.length, t.length <= 10^5
#  s and t consist of English letters.

# Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

# Follow up: Could you find an algorithm that runs in O(n) time?

# BCR: O(T)

# Approach 1. Brute
# For each c in t, O(T)
#   find index at s that's not duplicate. O(S)
# Return the minimum window
# O(TS), space: O(S)

# Approach 2. Frequency and queue
# Find frequencies of chars in t O(T)
# For each c in s, O(S)
#   Push c into queue and adjust frequench as needed.
#   if no frequencies are positive, consider it valid window. Find min of such
#   Pop from queue when valid
# O(S + T), space O(1) - only 26 English letters there

class Solution(object):
    def minWindow(self, s, t):
        freq, bag = {}, set()
        for c in t:
            freq[c] = freq.get(c, 0) + 1
            bag.add(c)
        
        min_window, left = None, 0
        for right, c in enumerate(s):
            if c in freq:
                freq[c] -= 1
                if freq[c] == 0: bag.remove(c)
                
            while len(bag) == 0:
                if not min_window or min_window[1] - min_window[0] > right - left:
                    min_window = [left, right]
                
                if s[left] in freq:
                    freq[s[left]] += 1
                    if freq[s[left]] > 0: bag.add(s[left])
                left += 1
        
        if not min_window: return ""
        
        return s[min_window[0]:min_window[1]+1]

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test(["ADOBECODEBANC", "ABC"], "BANC"),
    Test(["a", "a"], "a"),
    Test(["ADOBECODEBANC", "ABCZ"], ""),
]

solver = Solution()
for test in tests:
    print("{} {}".format(solver.minWindow(test.input[0], test.input[1]), test.output))
