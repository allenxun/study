class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def get(t):
            result = [1]
            left = 1
            for i in range(1,len(t)):
                result.append(left+t[i])
                left = t[i]
            result.append(1)
            return result
        
        result = []
        if rowIndex == 0:
            result = [1]
        elif rowIndex == 1:
            result = [1,1]
        else:
            result.append([1,1])
            for i in range(rowIndex):
                result = (get(result))
        return result

if __name__ =="__main__":
    a = Solution()
    test = [1,2,3,5,0]
    for i in test:
        print a.getRow(i)
