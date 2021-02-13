# Approach 1:
# Recurssively
#   Save children
#   Remove children
#   Append node as right child to temp tree's leaf
#   Visit children

class Solution(object):
    def flatten(self, root):
        if not root: return
        
        self.leaf = TreeNode()
        self.recurr(root)

    def recurr(self, node):
        if not node: return
    
        left, node.left = node.left, None
        right, node.right = node.right, None
        
        self.leaf.right = node
        self.leaf = self.leaf.right
        
        self.recurr(left)
        self.recurr(right)
