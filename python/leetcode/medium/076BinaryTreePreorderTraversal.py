class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        path = []
        self.preorder(root,path)
        return path
    def preorder(self,root,path):
        if root != None:
            path.append(root.val)
            self.preorder(root.left,path)
            self.preorder(root.right,path)
    def preorderTraversalIteratively(self,root):
        path = []
        stack = []
        while root != None or len(stack)>0:
            if root != None:
                while root:
                    path.append(root.val)
                    stack.append(root)
                    root = root.left
            else:
                print len(stack)
                root = stack[len(stack)-1].right
                stack.pop()
        return path


if __name__ == "__main__":
    tree1 = TreeNode(1)
    tree2 = TreeNode(2)
    tree3 = TreeNode(3)
    tree4 = TreeNode(4)
    tree5 = TreeNode(5)
    tree6 = TreeNode(6)
    tree7 = TreeNode(7)
    tree8 = TreeNode(8)

    tree1.right = tree2
    tree1.left  = tree3
    tree2.right = tree4
    tree2.left  = tree5
    tree3.right = tree6
    tree3.left  = tree7
    tree4.right = tree8
    tree4.left  = None
    tree5.right = None
    tree5.left  = None
    tree6.right = None
    tree6.left  = None
    tree7.right = None
    tree7.left  = None
    tree8.right = None
    tree8.left  = None

    a = Solution()
    print a.preorderTraversal(tree1)
    print a.preorderTraversalIteratively(tree1)
                 
