class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def order(self,root,level,result):
        if root:
            if len(result)<level+1:
                result.append([])
            result[level].append(root.val)
            self.order(root.left,level+1,result)
            self.order(root.right,level+1,result)
    def levelOrderBottom(self,root):
        result = []
        self.order(root,0,result)
        result.reverse()
        return result

if __name__ =="__main__":
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)

    t1.right = t2
    t1.left = t3
    a = Solution()
    print a.levelOrderBottom(t1)

