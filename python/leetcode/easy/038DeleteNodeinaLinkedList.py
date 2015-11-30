# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node == None:
            return None
        else:
            node.val = node.next.val
            node.next = node.next.next
            
if __name__ == "__main__":
    a = Solution()
    test1 = ListNode(1)
    test2 = ListNode(2)
    test3 = ListNode(3)
    test4 = ListNode(4)   
    test1.next = test2
    test2.next = test3
    test3.next = test4
    test4.next = None
    result = a.deleteNode(test2)
    print test1
