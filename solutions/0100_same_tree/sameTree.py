class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSameTree(p, q):
    if (p is None and q is None):
        return True
    elif ((p is None and q is not None) or (p is not None and q is None)):
        return False
    else:
        rootMatches = p.val == q.val
        leftMatches = isSameTree(p.left, q.left)
        rightMatches = isSameTree(p.right, q.right)

        return rootMatches and leftMatches and rightMatches