# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.isSymmetric0(root.left,root.right)
    def isSymmetric0(self,p,q):
        if p == None and q == None:
            return True
        if (p == None and q != None) or (p != None and q == None) or (p.val != q.val):
            return False
        return self.isSymmetric0(q.left,p.right) and self.isSymmetric0(p.left,q.right)

if __name__ == "__main__":
    tree1 = TreeNode(6)
    tree2 = TreeNode(2)
    tree3 = TreeNode(8)
    tree4 = TreeNode(0)
    tree5 = TreeNode(4)
    tree6 = TreeNode(7)
    tree7 = TreeNode(9)
    tree8 = TreeNode(3)
    tree9 = TreeNode(5)

    tree1.left = tree2
    tree1.right = tree3
    tree2.left = tree4
    tree2.right = tree5
    tree3.left = tree6
    tree3.right = tree7
    tree5.left = tree8
    tree5.right = tree9
    a = Solution()
    print a.isSymmetric(tree1)
