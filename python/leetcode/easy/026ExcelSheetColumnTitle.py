class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        if n<1:
            return ""
        result = ""
        strDict = {0:"Z",1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",\
            15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y"}
        while n:
            i = n%26
            if i == 0:
                n = n-1
            result = strDict[i] + result;
            n /= 26
        return result

if __name__  == "__main__":
    test = [1,26,27,28,64,676]
    a = Solution()
    for i in test:
        print a.convertToTitle(i)
