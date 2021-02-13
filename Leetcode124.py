# At each node, ask this question: "What is the best path sum from this node?"
# Then return either left path, right path, or only itself to its parent

class Solution(object):
    def maxPathSum(self, root):
        if not root: return 0

        self.maxSum = None
        self.recurr(root)
        return self.maxSum
    
    def recurr(self, node):
        if not node: return 0
        
        leftSum = self.recurr(node.left)
        rightSum = self.recurr(node.right)
        
        localSum = node.val
        if leftSum > 0: localSum += leftSum
        if rightSum > 0: localSum += rightSum
        
        if not self.maxSum or self.maxSum < localSum: self.maxSum = localSum
        
        return node.val + max(leftSum, rightSum, 0)
