class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
def invertTree(root):
    if root == None:
        return None
    else:
        tmp = root.left
        root.left = invertTree(root.right)
        root.right = invertTree(tmp)
        return root