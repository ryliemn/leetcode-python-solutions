import unittest
from sumOfLeftLeaves import sumOfLeftLeaves, TreeNode

class TestSumOfLeftLeaves(unittest.TestCase):
    def testGivenExample(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        returned = sumOfLeftLeaves(root)
        expected = 24

        self.assertEqual(returned, expected)

    def testRootOnly(self):
        root = TreeNode(1)

        returned = sumOfLeftLeaves(root)
        expected = 0

        self.assertEqual(returned, expected)

    def testAnotherTree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        returned = sumOfLeftLeaves(root)
        expected = 4

        self.assertEqual(returned, expected)


if __name__ == '__main__':
    unittest.main()