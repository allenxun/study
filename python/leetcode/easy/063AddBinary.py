class Solution(object):
    def addBinary1(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(str(int(a,2)+int(b,2))))[2:]
    def addBinary2(self, a, b):
        lena = len(a)
        lenb = len(b)
        if lena > lenb:
            b = '0' * (lena - lenb) + b
            lens = lena
        else:
            a = '0' * (lenb - lena) + a
            lens = lenb
        a = a[::-1]
        b = b[::-1]
        sum = ''
        carry = 0
        for i in range(lens):
            tmp = ord(a[i]) - 48 + ord(b[i]) - 48 + carry
            sum += str(tmp % 2)
            carry = tmp / 2
        if carry == 1:
            sum += '1'
        return sum[::-1]

if __name__ == "__main__":
    testa=["11","10","1"]
    testb=["11","11","11"]
    a = Solution()
    for i in range(len(testa)):
        print a.addBinary1(testa[i],testb[i])
        print a.addBinary2(testa[i],testb[i])
