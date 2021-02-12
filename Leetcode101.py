# The question is:
#   Is left subtree and right subtree the same?
#     Is left subtree of left subtree and right subtree of right subtree the same?
#     Is right subtree of left subtree and left subtree of right subtree the same?
#   ...

class Solution(object):
    def isSymmetric(self, root):
        if not root: return True
        
        stack_a, stack_b = [root.left], [root.right]
        while stack_a and stack_b:
            node_a = stack_a.pop(0)
            node_b = stack_b.pop(0)
            
            if not node_a and not node_b: continue
            if not node_a or not node_b or not node_a.val == node_b.val: return False
            
            stack_a += [node_a.left, node_a.right]
            stack_b += [node_b.right, node_b.left]
        
        if stack_a or stack_b: return False
        
        return True

    def _isSymmetric(self, root):
        if not root: return True
        
        return self.equal(root.left, root.right)
    
    def equal(self, a, b):
        if not a and not b: return True
        if not a or not b or not a.val == b.val: return False
        
        return self.equal(a.left, b.right) and self.equal(a.right, b.left)
