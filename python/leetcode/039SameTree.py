# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif p != None and q == None:
            return False
        elif p == None and q != None:
            return False
        elif p != None and q != None:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
if __name__ == "__main__":
    a = Solution()
    T1 = TreeNode(1)
    T2 = TreeNode(1)

    print a.isSameTree(T1,T2)
