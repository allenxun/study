class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        if n<1:
            return False
        if n==1:
            return True
        listNum = []
        flag = 1
        while(flag):
            s = 0
            while n:
                c = n%10
                n = n/10
                s = s+c*c
            n = s
            if s == 1:
                return True
            if s in listNum:
                flag = 0
                return False
            else:
                listNum.append(s)


if __name__ == "__main__":
    a = Solution()
    test = [19,1,4,99,100232]
    for i in test:
        print a.isHappy(i)
