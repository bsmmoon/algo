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
# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.

# Follow up: Can you solve it using O(1) (i.e. constant) memory?

# BCR: O(N)

# Approach 1:
#  Dump all nodes in a set while traversing.
#  If duplicate is found, return the node. If reach the tail, return None.
#  O(N), space: O(N)

# Approach 2:
#  Have a pointer move by 1 and another by 2.
#  If the faster reaches the tail, return False.
#  Else.. 
#  Let precycle = n, cycle = m
#  When slow reaches cycle, fast is n steps ahead of slow.
#  In other words, fast is m - n steps behind of slow.
#  After another m - n steps, fast catches slow.
#  So, in n + (m - n) = m steps, slow is caught.
#  At this point, the pointer is at m - n pos in the cycle.
#  Start another pointer from the beginning.
#  They should meet after n steps at the beginning of the cycle.
#  
#  O(N), space: O(1)

class Solution(object):
    def detectCycle(self, head):
        if not head or not head.next or not head.next.next: return
        
        slow, fast = head.next, head.next.next
        
        while True:
            if slow == fast: break
            if not fast or not fast.next or not fast.next.next: return
            slow = slow.next
            fast = fast.next.next
        
        start = head
        while slow != start:
            slow, start = slow.next, start.next
        return start
        

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test(([1], -1), None),
    Test(([3,2,0,-4], 1), 2),
    Test(([1,2], 0), 1),
    Test(([1,2], -1), None),
]

solver = Solution()
for test in tests:
    output = solver.detectCycle(makeCycledList(*test.input))
    print("{} {}".format(output.val if output else None, test.output))
