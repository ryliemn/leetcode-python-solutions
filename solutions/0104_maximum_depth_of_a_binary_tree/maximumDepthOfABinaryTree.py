class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root):
    return 0 if root == None else max(maxDepth(root.left), maxDepth(root.right)) + 1