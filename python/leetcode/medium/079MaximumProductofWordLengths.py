class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        nums = []
        sums = 0
        for i in words:
            for j in set(i):
                sums += 1<<(ord(j) - ord('a'))
            nums.append(sums)
            sums = 0
        
        result = 0
        for h in range(len(words)):
            for k in range(len(words)):
                if not (nums[h] & nums[k]):
                    result = max(len(words[h])*len(words[k]),result)

        return result
if __name__ == "__main__":
    test =[["abcw", "baz", "foo", "bar", "xtfn", "abcdef"],
           ["a", "ab", "abc", "d", "cd", "bcd", "abcd"],
           ["a", "aa", "aaa", "aaaa"]]

    a = Solution()

    for i in test:
        print a.maxProduct(i)
