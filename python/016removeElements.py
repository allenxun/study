# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        if head is None:
            return head 
        cur  = head
        next = head.next

        while next:
            if next.val == val:
                cur.next = next.next
                del next
                next = cur.next
            else:
                cur = cur.next
                next = next.next
        if head.val == val:
            cur = head
            head = head.next
            del cur
        return head

if __name__ == '__main__':
    head = ListNode(1)
    h1 = ListNode(1)
    h2 = ListNode(2)
   # h3 = ListNode(3)
   # h4 = ListNode(3)
   # h5 = ListNode(5)
    head.next = h1
    h1.next = h2
    h2.next = None
   # h3.next = h4
   # h4.next = h5
   # h5.next = None

    a = Solution()
    new = a.removeElements(head,1)
    while new:
        print new.val
        new = new.next
