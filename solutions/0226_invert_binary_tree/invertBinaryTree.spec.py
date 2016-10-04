import unittest
from invertBinaryTree import invertTree, TreeNode

class TestInvertTree(unittest.TestCase):
    def testGivenExample(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)

        returned = invertTree(root)

        self.assertEqual(returned.val, 4)
        self.assertEqual(returned.left.val, 7)
        self.assertEqual(returned.right.val, 2)
        self.assertEqual(returned.left.left.val, 9)
        self.assertEqual(returned.left.right.val, 6)
        self.assertEqual(returned.right.left.val, 3)
        self.assertEqual(returned.right.right.val, 1)

    def testRootOnly(self):
        root = TreeNode(1)

        returned = invertTree(root)

        self.assertEqual(returned.val, 1)
        self.assertIsNone(returned.left)
        self.assertIsNone(returned.right)

    def testUnevenTree(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.right = TreeNode(3)

        returned = invertTree(root)

        self.assertEqual(returned.val, 4)
        self.assertEqual(returned.left.val, 7)
        self.assertEqual(returned.right.val, 2)
        self.assertIsNone(returned.left.left)
        self.assertIsNone(returned.left.right)
        self.assertEqual(returned.right.left.val, 3)
        self.assertIsNone(returned.right.right)


if __name__ == '__main__':
    unittest.main()