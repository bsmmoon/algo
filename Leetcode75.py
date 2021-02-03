# Constraints:
#  n == nums.length
#  1 <= n <= 300
#  nums[i] is 0, 1, or 2.

# Basically, it's in-place sorting.

# Approach 1.
# Just.. count and populate??
# O(N)

# Approach 2. https://en.wikipedia.org/wiki/Dutch_national_flag_problem

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums) - 1
        
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
                
class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([2,0,2,1,1,0], [0,0,1,1,2,2]),
    Test([2,0,1], [0,1,2]),
    Test([0], [0]),
    Test([1], [1]),
]

solver = Solution()
for test in tests:
    solver.sortColors(test.input)
    print("{} {}".format(test.input, test.output))
