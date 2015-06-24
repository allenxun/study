#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA==None or headB == None:
            return None
        flagA = True
        flagB = True
        hA = headA
        hB = headB
        while(headA!=None and headB != None):
            if headA.val == headB.val:
                return headA
            headA = headA.next
            headB = headB.next
            if headA==None and flagA:
                headA = hB
                flagA = False
            if headB==None and flagB:
                headB = hA
                flagB = False
        return None

if __name__ == "__main__":
    h1 = ListNode(1)
    h2 = ListNode(2)
    h3 = ListNode(3)
    h4 = ListNode(4)
    
    l1 = ListNode(9)
    l2 = ListNode(3)
    l3 = ListNode(4)

    h1.next = h2
    h2.next = h3
    h3.next = h4
    h4.next = None

    l1.next = l2
    l2.next = l3
    l3.next = None
    
    a = Solution()
    print   a.getIntersectionNode(h1,l1).val
