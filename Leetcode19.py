# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Follow up: Could you do this in one pass?
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#
# BPR: O(n) - to access nth node
# APP1
# find sz O(sz)
# remove (sz-n)th node O(sz)
# O(sz)
# Traversed twice. Can do better?
# APP2
# let first pointer to move n ahead
# let first and second pointer to traverse until the first pointer reaches the end. second pointer is at (sz-n)th node
# O(sz), but in one pass

class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast = head
        for _ in range(n):
            fast = fast.next

        if not fast: return head.next

        slow = head
        while fast:
            fast = fast.next
            if not fast:
                slow.next = slow.next.next
                return head
            slow = slow.next

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def to_list(self):
        output = [self.val]
        curr = self.next
        while curr:
            output.append(curr.val)
            curr = curr.next
        return output

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
    Test([[1,2], 2], [2]),
]

solver = Solution()
for test in tests:
    output = solver.removeNthFromEnd(build_linked_list(test.input[0]), test.input[1])
    print(test.input, output.to_list() if output else [], test.output)
