class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        sTot = dict()
        tTos = dict()
        if len(s) != len(t):
            return False
        else :
            for i in range(len(s)):
                sTot[s[i]] = 0
                tTos[t[i]] = 0
            for i in range(len(s)):
                if sTot[s[i]] == 0:
                    if tTos[t[i]] == 0:
                        sTot[s[i]] = t[i]
                        tTos[t[i]] = s[i]
                    else:
                        return False
                else:
                    if sTot[s[i]] != t[i]:
                        return False
            return True
                

if __name__ == "__main__":
    a = Solution()
    test = [["add","egg"],["goo","bar"],["title","paper"],["asd","ers"],["aba","aab"]]
    for i in test:
        print a.isIsomorphic(i[0],i[1])
