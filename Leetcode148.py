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

# Constraints
# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105

# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

class Solution(object):
    def sortList(self, head):
        if not head or not head.next: return head
        
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        
        head = self.sortList(head)
        slow = self.sortList(slow)
        
        head = self.merge(head, slow)
        
        return head
        
    def merge(self, a, b):
        # print(a, b)
        curr = dummy = ListNode()
        
        while a and b:
            if a.val < b.val:
                curr.next, curr, a = a, a, a.next
            else:
                curr.next, curr, b = b, b, b.next
        
        curr.next = a if a else b

        return dummy.next

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([4,2,1,3], [1,2,3,4]),
    Test([-1,5,3,4,0], [-1,0,3,4,5]),
    Test([], None)
]



solver = Solution()
for test in tests:
    output = solver.sortList(makeLinkedList(test.input))
    print("{}\n{}".format(output, test.output))
