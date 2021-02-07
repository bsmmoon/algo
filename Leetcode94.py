# Constraints:
#  The number of nodes in the tree is in the range [0, 100].
#  -100 <= Node.val <= 100

# Follow up:
# Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            if not stack: return result
            
            node = stack.pop()
            result.append(node.val)
            root = node.right
        
    def recurr(self, root, inorder):
        if not root: return []
        self.recurr(root.left, inorder)
        inorder.append(root.val)
        self.recurr(root.right, inorder)
        return inorder
