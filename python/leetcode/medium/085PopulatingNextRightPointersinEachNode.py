class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root == None or root.left  == None:
            return
        root.left.next = root.right
        if root.next != None:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

if __name__ == "__main__":
    tree1 = TreeLinkNode(1)
    tree2 = TreeLinkNode(2)
    tree3 = TreeLinkNode(3)
    tree4 = TreeLinkNode(4)
    tree5 = TreeLinkNode(5)
    tree6 = TreeLinkNode(6)
    tree7 = TreeLinkNode(7)


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
    a.connect(tree1)
    print tree2.next
