# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Observations:
# 1. if depth of right subtree < depth of left subtree
#   subproblem starts from the right most node of the left subtree at depth of right subtree + 1
# 2. depth so far can be inferred from the number of nodes "seen" so far

# Approach
# while traversing in preorder but from right to left child
#   add node to view if depth is greater than current view

class Solution(object):
    def rightSideView(self, root):
        view = []
        self.addToView(view, root, 1)
        return view
    
    def addToView(self, view, node, depth):
        if not node: return
        if len(view) < depth: view.append(node.val)
        
        self.addToView(view, node.right, depth+1)
        self.addToView(view, node.left, depth+1)
