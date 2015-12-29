class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.path(root,sum,0)
    def path(self,node,sum,ss):
        if node == None:
            return False
        elif node.left== None and node.right == None:
            return ss+node.val == sum
        return self.path(node.left,sum,ss+node.val) or self.path(node.right,sum,ss+node.val)

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
    tree4.right = tree8

    a = Solution()
    print a.hasPathSum(tree1,111)
