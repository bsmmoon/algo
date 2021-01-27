# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

# Approach 1.
#  Just.. iterate. O(N), space: O(1)
#
# Approach 2.
#  Bsearch, but with modification
#  The goal is to find the boundary between the target value and its neighbours
#  Decrease the search space until either it is (non-target, target) or (target, non-target)
#  If (neighbour, target), and if mid is target,
#    then search left neighbour of mid, and if it's target, continue our search to left.
#  vice versa


class Solution(object):
    def searchRange(self, nums, target):
        if len(nums) == 0: return [-1, -1]
        if nums[0] == nums[-1]:
            return [0, len(nums)-1] if nums[0] == target else [-1, -1]
        return self.modified_bsearch(nums, target, 0, len(nums) - 1)
    
    def modified_bsearch(self, nums, target, left, right):
        if left > right: return [-1, -1]
        
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return [
                self.find_left_bound(nums, target, left, mid),
                self.find_right_bound(nums, target, mid, right)
            ]
        
        if nums[mid] < target:
            return self.modified_bsearch(nums, target, mid + 1, right)
        else:
            return self.modified_bsearch(nums, target, left, mid - 1)
            
    def find_left_bound(self, nums, target, left, right):
        mid = (left + right) // 2
        
        if nums[mid] == target:
            if mid == 0 or nums[mid - 1] != target: return mid
            return self.find_left_bound(nums, target, left, mid - 1)
        else:
            if nums[mid + 1] == target: return mid + 1
            return self.find_left_bound(nums, target, mid + 1, right)

    def find_right_bound(self, nums, target, left, right):
        mid = (left + right) // 2
        
        if nums[mid] == target:
            if mid + 1 == len(nums) or nums[mid + 1] != target: return mid
            return self.find_right_bound(nums, target, mid + 1, right)
        else:
            if nums[mid - 1] == target: return mid - 1
            return self.find_right_bound(nums, target, left, mid - 1)
        
class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([[0,0,1,1,1,1,2,2,2,3,3,4,5,6,6,6,6,7,8], 3], [9,10]),
    Test([[1,2,3,3,3,3,4,5,9], 3], [2,5]),
    Test([[1,1,2], 1], [0,1]),
    Test([[1,1,1,1], 1], [0,3]),
    Test([[1,1,1,1,2], 1], [0,3]),
    Test([[1,2,2,2,2], 1], [0,0]),
    Test([[1,2,2], 2], [1,2]),
    Test([[5,7,7,8,8,10], 8], [3,4]),
    Test([[5,7,7,8,8,10], 6], [-1,-1]),
    Test([[], 0], [-1,-1]),
]

solver = Solution()
for test in tests:
    print(solver.searchRange(test.input[0], test.input[1]), test.output)
