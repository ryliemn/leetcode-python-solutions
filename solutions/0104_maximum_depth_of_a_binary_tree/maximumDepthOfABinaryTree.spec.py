import unittest
from maximumDepthOfABinaryTree import maxDepth, TreeNode

class TestMaxDepth(unittest.TestCase):
    def testSmallTree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        returned = maxDepth(root)
        expected = 2

        self.assertEqual(returned, expected)

    def testUnevenTree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)

        returned = maxDepth(root)
        expected = 3

        self.assertEqual(returned, expected)

    def testRootOnlyTree(self):
        root = TreeNode(1)

        returned = maxDepth(root)
        expected = 1

        self.assertEqual(returned, expected)

    def testNoneTree(self):
        returned = maxDepth(None)
        expected = 0

        self.assertEqual(returned, expected)

if __name__ == '__main__':
    unittest.main()