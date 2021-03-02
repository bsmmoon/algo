# Idea
# swap left and right child.
# each child is its own subproblem

class Solution(object):
    def invertTree(self, node):
        if not node: return
    
        node.left, node.right = node.right, node.left
        self.invertTree(node.left)
        self.invertTree(node.right)
        
        return node
