# Let N be the size of the tree
# BCR: O(N), space: O(N)

# Approach 1. DFS
# Keep track of depth and append each nodes to its respective depth array
# O(N), space: O(N)

# Approach 2. modified BFS
# Enqueue children of current level to another queue and make it current once done
# O(N), space: O(N)

class Solution(object):
    def levelOrder(self, root):
        if not root: return []
        
        layers = [[]]
        self.traverse(root, layers, 0)
        return layers
    
    def traverse(self, node, layers, index):
        if not node: return
        
        if not index < len(layers): layers.append([])
        layers[index].append(node.val)
        
        self.traverse(node.left, layers, index + 1)
        self.traverse(node.right, layers, index + 1)
        
    def _levelOrder(self, root):
        if not root: return []
        
        current, children = [root], []
        layers = []
        while current:
            values = []
            for node in current:
                if node.left: children.append(node.left)
                if node.right: children.append(node.right)
                values.append(node.val)
            layers.append(values)
            current, children = children, []
        return layers
