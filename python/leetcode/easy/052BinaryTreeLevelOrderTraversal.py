class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.result = []
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.getNode(0,root)
        return self.result
    def getNode(self,dep,root):
        if root == None:
            return
        if len(self.result) > dep:
            self.result[dep].append(root.val)
        else:
            a = []
            a.append(root.val)
            self.result.append(a);
        self.getNode(dep + 1, root.left)
        self.getNode(dep + 1, root.right)

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
    tree2.left = None
    tree2.right = tree4
    tree3.left = tree5
    tree3.right = tree6
    tree4.left = tree7
    tree4.right = tree8

    a = Solution()
    print a.levelOrder(tree1)
