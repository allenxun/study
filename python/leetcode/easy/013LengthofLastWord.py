class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        while len(s)>0 and s[-1] == " ":
            s = s[0:-1]
        if len(s) == 0:
            return 0
        if len(s)>0:
            length = 0
            for i in s:
                if i != " ":
                    length = length+1
                else:
                    length = 0
            return length

if __name__ == "__main__":
    a = Solution()
    test = [""," ","  ","asdf","hello world","a ","a  "]
    for i in test:
        print a.lengthOfLastWord(i)
