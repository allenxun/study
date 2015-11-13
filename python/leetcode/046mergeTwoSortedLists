# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        p = result
 
        while(l1 != None and l2 != None):
          if l1.val <= l2.val:
              p.next = l1
              l1 = l1.next
          else:
              p.next = l2
              l2 = l2.next
 
          p = p.next
 
        if l1 != None:
            p.next = l1
        if l2 != None:
            p.next = l2
 
        return result.next

if __name__ == "__main__":
    a = Solution()
    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(6)
    node4 = ListNode(7)
    node5 = ListNode(19)
    node6 = ListNode(11)
    node7 = ListNode(12)
    node8 = ListNode(13)
    node9 = ListNode(17)
    node10 = ListNode(18)
    node11 = ListNode(20)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None

    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = node10
    node10.next = node11
    node11.next = None

    print a.mergeTwoLists(node1,node2)
