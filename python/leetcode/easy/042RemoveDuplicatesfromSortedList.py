# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head

        pre = head
        cur = head.next
        
        while cur !=None:
            if pre.val != cur.val:
                pre.next = cur
                pre = pre.next
            cur = cur.next
        pre.next = None
        return head

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(3)
    node4 = ListNode(2)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None

    a = Solution()
    a.deleteDuplicates(node1)
    cur = node1

    while cur != None:
        print cur.val
        cur = cur.next
