class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        cow = 0
        bull = 0
        secretlist = list(secret)
        guesslist = list(guess)
        temp = []
        for i in range(len(secretlist)):
            if secretlist[i] == guesslist[i]:
                bull += 1
                temp.append(secretlist[i])
            else:
                pass

        for i in temp:
            secretlist.remove(i)
            guesslist.remove(i)

        for i in guesslist:
            if i in secretlist:
                secretlist.remove(i)
                cow +=1
            else:
                pass
        return str(bull)+"A"+str(cow)+"B"

if __name__ == "__main__":
    testA = ["1807","1123","0111","1423","1122"]
    testb = ["7810","0111","1131","0411","2211"]
    a = Solution()
    for i in range(len(testA)):
        print a.getHint(testA[i],testb[i])

