class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        temp1 = {}
        set1 = set()
        temp2 = {}
        set2 = set()
        len1 = len(pattern)
        str = str.split(" ")
        
        if len(pattern) != len(str):
            return False
        for i in range(0,len1):
            if pattern[i] in temp1.keys():
                if str[i] != temp1[pattern[i]]:
                    return False
            else:
                if pattern[i] in set1:
                    return False
                temp1[pattern[i]] = str[i]
                set1.add(pattern[i])

            if str[i] in temp2.keys():
                if pattern[i] != temp2[str[i]]:
                    return False
            else:
                if str[i] in set2:
                    return False
                temp2[str[i]] = pattern[i]
                set2.add(str[i])
                
        return True

if __name__ == "__main__":
    test1 = ["hh bb cc","dog cat dog cat","dog cat cat fish","dog dog dog dog","dog cat cat dog"]
    test2 = ["abc","abba","abba","abba","abba"]
    a = Solution()

    for i in range(0,len(test1)):
        print a.wordPattern(test2[i],test1[i])

