# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def display(self):
        nodes = []
        curr = self
        while curr:
            if curr in nodes:
                print("{}, pos: {}".format(list(map(lambda x: x.val, nodes)), nodes.index(curr)))
                return
            
            nodes.append(curr)
            curr = curr.next
        print("{}, pos: -1".format(list(map(lambda x: x.val, nodes))))
            

def makeCycledList(arr, pos):
    nodes = []
    for val in arr:
        nodes.append(ListNode(val))
        if len(nodes) > 1: nodes[-2].next = nodes[-1]
    if pos in range(len(nodes)): nodes[-1].next = nodes[pos]
    return nodes[0]

# Constraints:
# The number of the nodes in the list is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a valid index in the linked-list.

# Follow up: Can you solve it using O(1) (i.e. constant) memory?

# BCR: O(N)

# Approach 1:
#  Dump all nodes in a set while traversing.
#  If duplicate is found, return True. If reach the tail, return False.
#  O(N), space: O(N)

# Approach 2:
#  Have a pointer move by 1 and another by 2.
#  If pointers meet, return True. If the faster reaches the tail, return False.
#  O(N), space: O(1)

class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next or not head.next.next: return False
        
        slow, fast = head.next, head.next.next
        
        while fast:
            if slow == fast: return True
            slow = slow.next
            fast = fast.next
            if not fast: return False
            fast = fast.next
        return False

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test(([3,2,0,-4], 1), True),
    Test(([1,2], 0), True),
    Test(([1,2], -1), False),
    Test(([1], -1), False),
]

solver = Solution()
for test in tests:
    print("{} {}".format(solver.hasCycle(makeCycledList(*test.input)), test.output))
