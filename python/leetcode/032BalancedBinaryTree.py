# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def checkDeepth(self,root):
        if root == None:
            return 0
        leftDeepth = self.checkDeepth(root.left)
        if leftDeepth == -1:
            return -1

        rightDeeptht = self.checkDeepth(root.right)
        if rightDeeptht == -1:
            return -1

        diffDeeptht = leftDeepth-rightDeeptht
        if abs(diffDeeptht)>1:
            return -1
        else:
            return max(leftDeepth+1,rightDeeptht+1)

    def isBalanced(self, root):
        if self.checkDeepth(root) == -1:
            return False
        else:
            return True

if __name__ == "__main__":
    a = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(1)
    n3 = TreeNode(1)
    n4 = TreeNode(1)
    n5 = TreeNode(1)
    n6 = TreeNode(1)
    n7 = TreeNode(1)
    
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    print a.isBalanced(n1)
