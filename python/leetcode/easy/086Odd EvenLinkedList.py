class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        p1 = head
        p2 = head.next
        result = head
        temp = head.next
        while p2 and p2.next:
            p1.next = p2.next
            p1 = p1.next
            p2.next = p1.next
            p2 = p2.next
        p1.next = temp
        return result 

if __name__ == "__main__":
    L1 = ListNode(1)
    L2 = ListNode(2)
    L3 = ListNode(3)
    L4 = ListNode(4)
    L5 = ListNode(5)
    L6 = ListNode(6)
    L7 = ListNode(7)
    L8 = ListNode(8)

    L1.next = L2
    L2.next = L3
    L3.next = L4
    L4.next = L5
    L5.next = L6
    L6.next = L7
    L7.next = L8
    L8.next = None

    a = Solution()

    a.oddEvenList(L1)

    head = L1
    while head:
        print head.val
        head = head.next
