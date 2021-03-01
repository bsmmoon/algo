# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        output = []
        curr = self
        while curr:
            output.append(curr.val)
            curr = curr.next
        return str(output)

def makeLinkedList(arr):
    if not arr: return

    head = ListNode(arr.pop(0))
    curr = head
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

# Approach 1. iterative
# while traversing,
#   prepend each node

class Solution(object):
    def reverseList(self, head):
        node = head
        pre, rhead = None, None
        while node:
            rhead, node = node, node.next
            rhead.next, pre = pre, rhead
        return rhead
        
class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([1,2,3,4,5], [5,4,3,2,1]),
    Test([1,2], [2,1]),
    Test([], []),
    Test([1], [1])
]

solver = Solution()
for test in tests:
    output = solver.reverseList(makeLinkedList(test.input))
    print("{} {}".format(output, test.output))
