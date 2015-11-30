class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        if len(str)==0:
            return 0
        strNum = ""
        negativeFlag = 1
        for i in range(len(str)):
            if str[i]!=" ":
                str = str[i:]
                break

        if str[0] not in ["-","+","0","9","8","7","6","5","4","3","2","1"]:
            return 0
        elif str[0] == "-":
            negativeFlag = -1
            str = str[1:]
        elif str[0] == "+":
            negativeFlag = 1
            str = str[1:]
        for i in range(len(str)):
            if str[i]!="0":
                str = str[i:]
                break

        for i in range(len(str)):
            if i in ["-","+"," "]:
                return 0
            if "0"<=str[i]<="9":
                strNum +=str[i]
            else:
                break
        
        if len(strNum)==0:
            return 0
        num = int(strNum)*negativeFlag
        if num>2147483647:
            return 2147483647
        elif num<-2147483648:
            return -2147483648
        else:
            return num
if __name__ == "__main__" :
    test = ["","   123","-123"," +123","12bdc33","b12","0123",'abc',"--2","1-2","1 2",' - 1',"+-2","-+1"]
    a = Solution()
    for i in test:
        print a.myAtoi(i)
                
