# Let N be the size of the tree
# BCR: O(N)

# Approach 1. DFS
# O(N), space: O(log(N))

# Approach 2. modified BFS
# O(N), space: O(2^(N-1))

class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        
        return self.traverse(root, 0)
    
    def traverse(self, node, index):
        if not node: return index
        
        return max(
            self.traverse(node.left, index + 1),
            self.traverse(node.right, index + 1)
        )
        
    def _maxDepth(self, root):
        if not root: return 0
        
        current, children = [root], []
        depth = 1
        while current:
            for node in current:
                if node.left: children.append(node.left)
                if node.right: children.append(node.right)
            
            if not children: break
            
            current, children = children, []
            depth += 1
        return depth
