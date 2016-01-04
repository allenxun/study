class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
    def strStr(self, haystack, needle):  
        lenH, lenN = len(haystack), len(needle)  
        if lenN == 0:  
            return 0  
        if lenN > lenH or lenH == 0:  
            return -1  
  
        rolling = lambda x, y: x * 29 + y  
        get_hash = lambda ch: ord(ch) - ord('a')  
  
        nhash = reduce(rolling, map(get_hash, needle))  
        hhash = reduce(rolling, map(get_hash, haystack[:lenN]))  
        if nhash == hhash:  
            return 0  
  
        high_base = 29 ** (lenN - 1)  
        for i in range(lenN, lenH):  
            hhash -= get_hash(haystack[i - lenN]) * high_base 
            hhash = rolling(hhash, get_hash(haystack[i]))     
            if nhash == hhash:  
                return i - lenN + 1  
  
        return -1 
    def strStr1(self, haystack, needle):
        lenH=len(haystack);lenN=len(needle)
        next=[-1 for i in range(lenN+1)]
        self.getNext(needle,next,lenN)
        i=0;j=0
        while i<lenH and j<lenN:
            if j==-1 or haystack[i]==needle[j]:
                i+=1;j+=1
            else:
                j=next[j]
        if j<lenN:
            return -1
        else:
            return i-lenN
    def getNext(self,needle,next,lenN):
        i=0;j=-1
        while i<lenN:
            if j==-1 or needle[i]==needle[j]:
                i+=1
                j+=1
                next[i]=j
            else:
                j=next[j]

if __name__ == "__main__":
    a = Solution()
    testa = ["ab","abc","dd","issip"]
    testb = ["987abc","abc","9966","mississippi"]
    for i in range(len(testa)):
        print a.strStr(testb[i],testa[i])
        print a.strStr1(testb[i],testa[i])
