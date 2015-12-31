class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = head
        p2 = head
        
        if head == None:
            return None
        
        for i in range(0,n):
            p1 = p1.next

        if p1 == None:
            return head.next

        else:
            while p1.next != None:
                p1 = p1.next
                p2 = p2.next
            p2.next = p2.next.next
            return head

if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None
    
    a = Solution()
    t = a.removeNthFromEnd(n1,2)
    while t != None:
        print t.val
        t = t.next
    
