class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]
        for i in range(1,num+1):
            result.append(result[i>>1]+(i&1))
        return result


if __name__ == "__main__":
    a = Solution()
    test = 19
    print a.countBits(19)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
