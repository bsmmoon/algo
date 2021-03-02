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

# Approach 1.
# slow and fast runner
# slow runner invert the link on the wa
# when fast reaches the end,
# compare slow runner and inverted list
# O(N), space: O(1)

class Solution(object):
    def isPalindrome(self, head):
        prepre, pre = None, None
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow, prepre, pre = slow.next, pre, slow
            pre.next = prepre
        
        if fast and not fast.next: slow = slow.next
        
        while slow and pre:
            if slow.val != pre.val: return False
            slow, pre = slow.next, pre.next
        return True
            
            
class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([1], True),
    Test([1,2], False),
    Test([1,2,2], False),
    Test([1,2,2,1], True),
    Test([1,2,3,2,1], True),
]

solver = Solution()
for test in tests:
    output = solver.isPalindrome(makeLinkedList(test.input))
    print("{} {}".format(output, test.output))
            
        
