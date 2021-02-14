# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
        
    def display(self):
        curr = self
        while curr:
            print(
                curr.val,
                curr.next.val if curr.next != None else None,
                curr.random.val if curr.random != None else None)
            curr = curr.next
        
def makeLL(arr):
    if not arr: return None
    
    root = Node(arr[0][0], None, arr[0][1])
    curr = root
    nodes = [root]
    for pair in arr[1:]:
        curr.next = Node(pair[0], None, pair[1])
        curr = curr.next
        nodes.append(curr)
    
    curr = root
    while curr:
        if curr.random != None: curr.random = nodes[curr.random]
        curr = curr.next
    return root

# Constraints
#  0 <= n <= 1000
#  -10000 <= Node.val <= 10000
#  Node.random is null or is pointing to some node in the linked list.

# Approach 1.
#  for each node
#   create node with value and add to array
#   set value of the original node as its index
#  iterate both lists
#    use the original's value as index to the array of nodes
# O(N), O(N)

class Solution(object):
    def copyRandomList(self, head):
        if not head: return None
        
        nodes = []
        curr = head
        
        nodes.append(Node(curr.val))
        curr.val = len(nodes) - 1
        curr = curr.next
        while curr:
            nodes.append(Node(curr.val))
            nodes[-2].next = nodes[-1]
            curr.val = len(nodes) - 1
            curr = curr.next
        
        curr = head
        for node in nodes:
            if curr.random: node.random = nodes[curr.random.val]
            curr = curr.next
        
        return nodes[0]
        
class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([[7,None],[13,0],[11,4],[10,2],[1,0]], [[7,None],[13,0],[11,4],[10,2],[1,0]]),
    Test([[1,1],[2,1]], [[1,1],[2,1]]),
    Test([[3,None],[3,0],[3,None]], [[3,None],[3,0],[3,None]]),
    Test([], [])
]

solver = Solution()
for test in tests:
    print("{} {}\n".format(solver.copyRandomList(makeLL(test.input)), test.output))
