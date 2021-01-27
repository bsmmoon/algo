# Constraints:
# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is guaranteed to be rotated at some pivot.
# -104 <= target <= 104

# Approach 1
# Just.. iterate. O(N), space: O(1)
#
#  Rotated array will contain the original array when appended by itself
#  But this operation will cost O(N).. which means it won't do better than Approach 1
#
# Approach 2
#  Bsearch, but with modification
#  ex. for [[4,5,6,7,8,9,0], 0]
#  it will check midpoint and go left as per usual bsearch
#  but until the end, it won't find 0.
#  then check the right side of the initial midpoint [8,9,0]
#  same thing happend, and search [0]. Now it's found.
#  O(N), space: O(1)

class Solution(object):
    def search(self, nums, target):
        return self.modified_bsearch(nums, target, 0, len(nums) - 1)
        
    def modified_bsearch(self, nums, target, left, right):
        if left > right: return -1
        
        mid = (left + right) // 2

        if nums[mid] == target: return mid
        
        if nums[mid] < target:
            result = self.modified_bsearch(nums, target, mid + 1, right)
            if nums[left] > nums[right] and result == -1:
                result = self.modified_bsearch(nums, target, left, mid - 1)
        else:
            result = self.modified_bsearch(nums, target, left, mid - 1)
            if nums[left] > nums[right] and result == -1:
                result = self.modified_bsearch(nums, target, mid + 1, right)
        
        return result

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([[0,1,2,4,5,6,7], 0], 0),
    Test([[4,5,6,7,0,1,2], 0], 4),
    Test([[4,5,6,7,0,1,2], 3], -1),
    Test([[1], 0], -1),
    Test([[5,1,3], 5], 0)
]

solver = Solution()
for test in tests:
    print(solver.search(test.input[0], test.input[1]), test.output)
