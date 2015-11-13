# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None or p == None or q == None:
            return None
        if max(q.val,p.val)<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif min(q.val,p.val) > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
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

    a=Solution()
    print a.lowestCommonAncestor(tree1,tree3,tree4).val
