class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        listTest = [False for i in range(n+2)]
        listTest[0] = True
        listTest[1] = True
        num = 0
        i=2
        j=1
        while i*i<n:
            if listTest[i] == False:
                j = i
                while i*j<n:
                    listTest[i*j] = True
                    j = j+1
            i = i+1

        for i in range(n):
            if listTest[i] == False:
                num = num+1
        return num
if __name__ == "__main__":
    a = Solution()
    test = [3,4,5,50000]
    for i in test:
        print a.countPrimes(i)
