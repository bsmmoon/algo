# Constraints:
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= start_i <= end_i <= 10^4

# Let N = intervals.length

# BCR: O(N), space O(N)

# Can I assume that the intervals are sorted? The examples seem that way..
# Approach 1.
# Set start as left and end as right.
# If the next one overlaps, set its end as right.
# Else, set it as a new interval.
# Repeat.
# O(N), space: O(N)

# Ok, so the assumption was wrong :p
# Sort and do Approach 1
# O(NlogN), space O(N)

class Solution(object):
    def merge(self, intervals):
        if len(intervals) == 0: return []
        
        intervals = sorted(intervals, key=lambda x: x[0])
        
        merged_intervals = []
        left, right = intervals[0]
        for interval in intervals[1:]:
            if left <= interval[0] <= right:
                right = max(right, interval[1])
            else:
                merged_intervals.append((left, right))
                left, right = interval
        merged_intervals.append((left, right))
        return merged_intervals
        
    def overlapping(self, a, b):
        return not (a[1] <= b[0] or b[1] <= a[0])

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
    Test([[1,4],[4,5]], [[1,5]]),
    Test([[1,4],[0,4]], [[0,4]]),
    Test([[2,3],[4,5],[6,7],[8,9],[1,10]], [[1,10]])
]

solver = Solution()
for test in tests:
    print("{}\n{}".format(solver.merge(test.input), test.output))
