class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: result
        """
        result = "1"
        for i in range(n-1):
            temp = result
            result = ""
            c = temp[0]
            count = 1
            for j in range(1,len(temp)):
                if temp[j] == temp[j-1]:
                    count += 1
                else:
                    result += (str(count) + temp[j-1])
                    count = 1
            result += (str(count) + temp[len(temp)-1])
        return result
        
if __name__ == "__main__":
    test =[1,2,3,4,5,6]
    a = Solution()
    for i in test:
        print a.countAndSay(i)
