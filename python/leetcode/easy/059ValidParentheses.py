class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = []
        for i in s:
            if i in [")","]","}"]:
                if len(temp) == 0:
                    return False
                else:
                    c = temp.pop()
                    if (c == "(" and i != ")") or (c == "[" and i != "]") or (c == "{" and i != "}"):
                        return False
            else:
                temp.append(i)
        return len(temp) == 0

if __name__ == "__main__":
    test = ["()","{{}","{[()]}"]
    a = Solution()
    for i in test:
        print a.isValid(i)
