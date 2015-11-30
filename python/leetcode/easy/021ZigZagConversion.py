class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        src = ''
        list = ''
        if numRows<=1:
            return s
        if numRows == 2:
            for i in range(len(s)):
                if i%2==0:
                    src = src+s[i]
                else:
                    list = list+s[i]
            return src+list

        list = ["" for i in range(numRows)]
        list[0]=s[0]
        time = 1
        num = 1
        for i in range(1,len(s)):
            if time == 1:
                if num == numRows-2:
                    time = 0
                list[num]=list[num]+s[i]
                num = num+1
                continue
            if time == 0:
                if num == 1:
                    time = 1
                list[num]=list[num]+s[i]
                num = num -1
                continue
        

        for i in list:
            src = src+i
        return src
             


if __name__ == "__main__":
    test = ["asdfg","abcdefghijklmnopqrstuvwxz",""]
    a = Solution()
    print a.convert("abc",2)
    print a.convert("PAYPALISHIRING",3)
    #for i in test:
   #     print a.convert(i,4)
