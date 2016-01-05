class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.inorder(root,result)
        return result
    def inorder(self,root,result):
        if root != None:
            if root.left != None:
                self.inorder(root.left,result)
            result.append(root.val)
            if root.right != None:
                self.inorder(root.right,result)
    def inorderTraversalIteratively(self,root):
        result = []
        stack = []
        while root != None or len(stack)>0:
            while root != None:
                stack.append(root)
                root = root.left
            if len(stack)>0:
                root = stack[len(stack)-1]
                result.append(root.val)
                stack.pop()
                root = root.right
        return result

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
    print a.inorderTraversal(tree1)
    print a.inorderTraversalIteratively(tree1)
