class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if head == None or head.next == None:
            return True
        if head.next.next == None:
            if head.val == head.next.val:
                return True
            else:
                return False

        last = self.getReverse(head)

        while head != None and last != None:
            if head.val != last.val:
                return False
            head = head.next
            last = last.next
        return True
    def getReverse(self,head):
        p1 = head
        p2 = head
        while p1 != None and p1.next != None:
            p1 = p1.next.next
            p2 = p2.next
        if p1 != None:
            p2.next = self.reverse(p2.next)
            p2 = p2.next
        else:
            p2 = self.reverse(p2)
        return p2
    def reverse(self,head):
        if head == None or head.next == None:
            return head
        else:
            newHead = self.reverse(head.next)
            head.next.next = head
            head.next = None
            return newHead

if __name__ == "__main__":
    h0 = ListNode(3)
    h1 = ListNode(2)
    h2 = ListNode(1)
    h3 = ListNode(0)
    h4 = ListNode(1)
    h5 = ListNode(2)
    h6 = ListNode(3)

    h0.next = h1
    h1.next = h2
    h2.next = h3
    h3.next = h4
    h4.next = h5
    h5.next = h6
    h6.next = None

    a = Solution()

    print a.isPalindrome(h0)

