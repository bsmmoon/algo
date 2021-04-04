class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.max = 0
        self.visit(root, 0)
        return self.max

    def visit(self, node, depth):
        if not node.left and not node.right: return depth
        
        left = self.visit(node.left, depth+1) if node.left else 0
        right = self.visit(node.right, depth+1) if node.right else 0
        self.max = max(self.max, left + right - depth * 2)
        return max(left, right)
