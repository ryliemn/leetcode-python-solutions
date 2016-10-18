class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(node):
    # while node.next != None:
    #     node.val = node.next.val
    #     if node.next.next == None:
    #         node.next = None
    #     else:
    #         node = node.next
    node.val = node.next.val
    node.next = node.next.next
    