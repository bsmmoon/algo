class Solution(object):
    def kthSmallest(self, root, k):
        self.k = k
        
        return self.inorderSearchKth(root)
        
    def inorderSearchKth(self, node):
        if not node: return
        
        val = self.inorderSearchKth(node.left)
        if val != None: return val
        
        self.k -= 1
        if self.k == 0: return node.val
        
        val = self.inorderSearchKth(node.right)
        if val != None: return val
        
        return
