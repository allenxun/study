# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root == None:
            return None
        if root.left == None and root.right == None:
            return root
        temp = None
        if root.right:
            temp = root.right
        if root.left:
            root.right = root.left
            root.left = temp
        else:
            root.right = None
            root.left = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

if __name__ == "__main__":
    t0 = TreeNode(0)
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)

    t0.left = t1
    t0.right = t2
    t1.left = t3
    t1.right = t4
    t2.left = t5
    t2.right = t6

    a = Solution()
    
    print t0.val,t0.left.val,t0.right.val,t1.left.val,t1.right.val,t2.left.val,t2.right.val
    a.invertTree(t0)
    print t0.val,t0.left.val,t0.right.val,t1.left.val,t1.right.val,t2.left.val,t2.right.val
