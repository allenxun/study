class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        p1 = head
        p2 = head
        
        while p1 != None and p1.next != None:
            p2 = p2.next
            p1 = p1.next.next
            if p1 == p2:
                return True
        return False

if __name__ == "__main__":
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(5)
    p6 = ListNode(6)
    p7 = ListNode(7)
    p8 = ListNode(8)
    p9 = ListNode(9)

    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p1
    p5.next = p6
    p6.next = p7
    p7.next = p8
    p8.next = p9
    p9.next = None

    a = Solution()
    print a.hasCycle(p1)
    print a.hasCycle(p5)
