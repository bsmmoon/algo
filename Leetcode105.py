# first element of preorder is the root
# left side of root in inorder is left subtree
# nodes in left subtree entails the root in preorder
class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder: return
    
        root = TreeNode(preorder[0])
        leftsize = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:leftsize+1], inorder[:leftsize])
        root.right = self.buildTree(preorder[leftsize+1:], inorder[leftsize+1:])
        return root

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

tests = [
    Test([[3,9,20,15,7], [9,3,15,20,7]], [3,9,20,None,None,15,7]),
]

solver = Solution()
for test in tests:
    print("{} {}".format(solver.buildTree(test.input[0], test.input[1]), test.output))
