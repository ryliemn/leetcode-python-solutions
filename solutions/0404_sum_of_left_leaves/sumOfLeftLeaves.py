class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sumOfLeftLeaves(root):
    def sumOfLeftLeavesHelper(root, isLeft):
        if root == None:
            return 0
        else:
            hasLeftChild = root.left != None
            hasRightChild = root.right != None
            isLeaf = not hasLeftChild and not hasRightChild
            if isLeft and isLeaf:
                return root.val
            else:
                leftSum = sumOfLeftLeavesHelper(root.left, True)
                rightSum = sumOfLeftLeavesHelper(root.right, False)
                return leftSum + rightSum
        
    return sumOfLeftLeavesHelper(root, False)