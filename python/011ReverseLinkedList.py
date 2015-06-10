# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    # iteratively
    def reverseListIteratively(self, head):
        new = None
        cur = head
        newHead = head
        if head is None or head.next == None:
            return head

        while cur:
            newHead = cur 
            temp = cur.next
            cur.next = new
            new = cur 
            cur = temp
        return newHead
    # recursively
    def reverseListRecursively(self,head):
        if head is None or head.next == None:
            return head
        else:
            newHead =  self.reverseListRecursively(head.next)
            head.next.next = head
            head.next = None
            return newHead

if __name__ == '__main__':
    head = ListNode(0)
    h1 = ListNode(1)
    h2 = ListNode(2)
    h3 = ListNode(3)
    h4 = ListNode(4)
    h5 = ListNode(5)
    head.next = h1
    h1.next = h2
    h2.next = h3
    h3.next = h4
    h4.next = h5
    h5.next = None

    a = Solution()

    new1 = a.reverseListRecursively(head)
    while new1:
        print new1.val
        new1 = new1.next
'''
    new = a.reverseListIteratively(head)
    while new:
        print new.val
        new = new.next

    newhead = None
    new1 = a.reverseListRecursively(head,newhead)
    while new1:
        print new1.val
        new1 = new1.next
'''
