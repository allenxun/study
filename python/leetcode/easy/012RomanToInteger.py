class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        RTI = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return RTI[s]
        if len(s) >= 2:
            result = RTI[s[0]]
            for i in range(1,len(s)):
                cur = RTI[s[i]]
                pre = RTI[s[i-1]]
                if cur<=pre:
                    result = cur+result
                else:
                    result = cur+result-2*pre
            return result



if __name__ == "__main__":
    a = Solution()
    test = ["","I","II","VI","IV","MCD","MMMCMXCIX"]
    for i in test:
        print a.romanToInt(i)
