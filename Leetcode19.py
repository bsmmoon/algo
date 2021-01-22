# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

class Solution(object):
    def removeNthFromEnd(self, head, n):
        return []

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def print(self):
        output = str(self.val)
        curr = self.next
        while curr:
            output += "-" + str(curr.val)
            curr = curr.next
        print(output)

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

def build_linked_list(values):
    curr = root = ListNode(values[0])
    for value in values[1:]:
        curr.next = ListNode(value)
        curr = curr.next
    return root

tests = [
    Test([[1,2,3,4,5], 2], [1,2,3,5]),
    Test([[1], 1], []),
    Test([[1,2], 1], [1]),
]

solver = Solution()
for test in tests:
    print(solver.removeNthFromEnd(build_linked_list(test.input[0]), test.input[1]), test.output)
