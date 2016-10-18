import unittest
from deleteNodeInALinkedList import deleteNode, ListNode

class TestDeleteNode(unittest.TestCase):
    def testGivenExample(self):
        node = ListNode(1)
        node.next = ListNode(2)
        node.next.next = ListNode(3)
        node.next.next.next = ListNode(4)

        deleteNode(node.next.next)

        self.assertEqual(node.val, 1)
        self.assertEqual(node.next.val, 2)
        self.assertEqual(node.next.next.val, 4)
        self.assertEqual(node.next.next.next, None)

    def testFirstNodeDeletion(self):
        node = ListNode(1)
        node.next = ListNode(2)
        node.next.next = ListNode(3)
        node.next.next.next = ListNode(4)

        deleteNode(node)

        self.assertEqual(node.val, 2)
        self.assertEqual(node.next.val, 3)
        self.assertEqual(node.next.next.val, 4)

if __name__ == '__main__':
    unittest.main()