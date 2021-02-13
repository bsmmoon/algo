# Constraints:
#  0 <= nums.length <= 10^4
#  -10^9 <= nums[i] <= 10^9

# Follow up: Could you implement the O(n) solution?

# Observations:
#  - There can be duplicates
#  - each sequence is actually just a range

# Approach 1.
# for each num O(N)
#   find group by using hash O(1)
#   add it to the group or create a new group O(1)
#   merge if necessary O(1)
# O(N), space: O(N)

# Approach 2.
# Since set's remove is O(1)
# for each num
#   find all its sequences and remove
# O(N), space: O(1)


class Solution(object):
    def longestConsecutive(self, nums):
        if not nums: return 0
        
        nums = set(nums)
        
        longest, count = 0, 0
        while nums:
            num = nums.pop()
            count = 1
            
            succ = num + 1
            while succ in nums:
                nums.remove(succ)
                succ += 1
                count += 1
            
            pred = num - 1
            while pred in nums:
                nums.remove(pred)
                pred -= 1
                count += 1
            
            if longest < count: longest = count
        return longest
    
    def _longestConsecutive(self, nums):
        if not nums: return 0
        
        nums = set(nums)
        
        longest = 0
        counter, groups = {}, {}
        for num in nums:
            if num - 1 in groups:
                preroot = self.findRoot(groups, num - 1)
                groups[num] = preroot
                counter[preroot] += 1
                if num + 1 in groups:
                    sucroot = self.findRoot(groups, num + 1)
                    groups[sucroot] = groups[preroot]
                    counter[preroot] += counter[sucroot]
                if longest < counter[preroot]: longest = counter[preroot]
            elif num + 1 in groups:
                root = self.findRoot(groups, num + 1)
                groups[num] = root
                counter[root] += 1
                if longest < counter[root]: longest = counter[root]
            else:
                groups[num] = num
                counter[num] = 1
                if longest < counter[num]: longest = counter[num]

        return longest
        
        
    def findRoot(self, groups, num):
        while num != groups[num]: num = groups[num]
        return num

class Group():
    def __init__(self, val):
        self.min = val
        self.max = val
    
    

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([9,1,4,7,3,-1,0,5,8,-1,6], 7),
    Test([100,4,200,1,3,2], 4),
    Test([0,3,7,2,5,8,4,6,0,1], 9),
    Test([0,3,4,2,5,8,7,6,0,1], 9),
]

solver = Solution()
for test in tests:
    print("{} {}".format(solver.longestConsecutive(test.input), test.output))
