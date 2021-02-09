# Constraints:
#  The number of nodes in the tree is in the range [1, 10^4].
#  -2^31 <= Node.val <= 2^31 - 1

# Observation:
#  a node's value is an upper bound for left subtree and lower bound for right subtree

# BCR: O(N)

# Approach 1:
#  Do inorder traversal. O(N)
#  Check if all are in order. O(N)
#  O(N), space: O(N)

# Approach 2.
#  While in DFS O(N)
#   Update upper bound and lower bound and check O(1)
#  O(N), space: O(1)

class Solution(object):
    def isValidBST(self, root):
        return self.checkBound(root, pow(2, 31) * -2, pow(2, 31))
        
    def checkBound(self, node, lowerBound, upperBound):
        if not node: return True
        if not (lowerBound < node.val < upperBound): return False
        return self.checkBound(node.left, lowerBound, node.val) and \
            self.checkBound(node.right, node.val, upperBound)
        
        
    def _isValidBST(self, root):
        arr = self.inorderTraversal(root)
        for i, v in enumerate(arr[:len(arr)-1]):
            if not v < arr[i+1]: return False
        return True
        
    def inorderTraversal(self, node, arr=[]):
        if node.left: arr = arr + self.inorderTraversal(node.left)
        arr = arr + [node.val]
        if node.right: arr = arr + self.inorderTraversal(node.right)
        return arr
        

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.size = 1

    def insert(self, val):
        if not val:
            self.size += 1
            return
    
        depth = 1
        while self.size >= pow(2, depth): depth += 1

        if self.size == pow(2, depth) - 1:
            nodesInLastDepth = 0
        else:
            nodesInLastDepth = self.size - (pow(2, depth - 1) - 1)
        maxNodesInLastDepth = pow(2, depth - 1)

        if nodesInLastDepth < maxNodesInLastDepth / 2:
            if not self.left:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
        else:
            if not self.right:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)
    
        self.size += 1
        
    def display(self):
        layer = []
        queue = [self]
        print([self.val])
        while any(node for node in queue):
            nextQueue = []
            while queue:
                node = queue.pop(0)
                if not node:
                    layer += [None, None]
                    nextQueue += [None, None]
                else:
                    layer += [
                        node.left.val if node.left else None,
                        node.right.val if node.right else None
                    ]
                    nextQueue += [node.left, node.right]
            print(layer)
            layer = []
            queue = nextQueue

def makeTree(arr):
    if len(arr) == 0: return

    root = TreeNode(arr[0])
    for val in arr[1:]:
        root.insert(val)
    return root
        
class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([2,1,3], True),
    Test([5,1,4,None,None,3,6], False),
]

solver = Solution()
for test in tests:
    print("{} {}".format(solver.isValidBST(makeTree(test.input)), test.output))
