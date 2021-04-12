# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# value,left,right,value,left,right,etc...

# v1
# 1,3,6,2,,,3,9,12,4,,,5,,

# v2
# 1,1,2,2,,,3,3,4,4,,,5,,

class Codec:
    def __init__(self):
        self.separator = ","

    def serialize(self, root):
        self.tokens = []
        
        self.visitNode(root)
        
        return self.separator.join(map(lambda x: "" if x is None else str(x), self.tokens))
    
    def visitNode(self, node):
        if not node: return
    
        index = len(self.tokens)
        self.tokens += [node.val, None, None]
        if node.left: self.tokens[index+1] = int(self.visitNode(node.left)/3)
        if node.right: self.tokens[index+2] = int(self.visitNode(node.right)/3)
        return index

    def deserialize(self, data):
        tokens = map(lambda x: None if x == "" else int(x), data.split(self.separator))
        return self.revisitNode(tokens, 0)
        
    def revisitNode(self, tokens, index):
        if not index+2 < len(tokens): return
    
        val, left, right = tokens[index:index+3]
    
        node = TreeNode(val)
        if left: node.left = self.revisitNode(tokens, left*3)
        if right: node.right = self.revisitNode(tokens, right*3)
        return node
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
