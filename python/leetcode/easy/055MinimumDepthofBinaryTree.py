class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import sys
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0 and right == 0:
            return 1
        elif left == 0:
            left = sys.maxint
        elif right == 0:
            right = sys.maxint
        return min(left,right)+1

if __name__ == "__main__":

    tree1 = TreeNode(1)
    tree2 = TreeNode(2)
    tree3 = TreeNode(3)
    tree4 = TreeNode(4)
    tree5 = TreeNode(5)
    tree6 = TreeNode(6)
    tree7 = TreeNode(7)
    tree8 = TreeNode(8)
    tree9 = TreeNode(9)

    tree1.left = tree2
    tree1.right = tree3
    tree2.left = tree9
    tree2.right = tree4
    tree3.left = tree5
    tree3.right = tree6
    tree4.left = tree7
    tree4.right = None

    a = Solution()
    print a.minDepth(tree4)
