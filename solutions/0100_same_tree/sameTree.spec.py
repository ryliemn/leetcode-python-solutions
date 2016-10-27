import unittest
from sameTree import isSameTree, TreeNode

class TestSameTree(unittest.TestCase):
    def testEqualTree(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)

        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)

        returned = isSameTree(p, q)
        expected = True

        self.assertEqual(returned, expected)

    def testDifferentNode(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(4)

        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)

        returned = isSameTree(p, q)
        expected = False

        self.assertEqual(returned, expected)

    def testUnevenTree(self):
        p = TreeNode(1)
        p.left = TreeNode(2)

        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)

        returned = isSameTree(p, q)
        expected = False

        self.assertEqual(returned, expected)

if __name__ == '__main__':
    unittest.main()