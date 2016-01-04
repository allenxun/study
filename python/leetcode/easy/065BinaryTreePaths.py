class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.result = []
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root != None:
            self.result.append(self.getPath(root,str(root.val)))
        if None in self.result:
            self.result.remove(None)
        return self.result

    def getPath(self,root,val):
        if root.left == None and root.right == None:
            self.result.append(val)
        if root.left != None:
            self.getPath(root.left,val+"->"+str(root.left.val))
        if root.right != None:
            self.getPath(root.right,val+"->"+str(root.right.val))

if __name__ == "__main__":
    tree1  = TreeNode(1)
    tree2  = TreeNode(2)
    tree3  = TreeNode(3)
    tree4  = TreeNode(4)
    tree5  = TreeNode(5)
    tree6  = TreeNode(6)
    tree7  = TreeNode(7)

    tree1.left = tree2
    tree1.right = tree3
    tree2.left = tree4
    tree2.right = tree5
    tree3.left = tree6
    tree3.right = tree7

    tree4.left = None
    tree4.right = None
    tree5.left = None
    tree5.right = None
    tree6.left = None
    tree6.right = None
    tree7.left = None
    tree7.right = None

    a = Solution()
    print a.binaryTreePaths(tree1)
              
