class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        length =1
        count = 9
        start = 1

        while (n > length * count):
            n -= length  * count;
            length = length + 1;
            count  = count * 10;
            start  = start * 10;

        start += (n - 1) / length;
        t = str(start);
        return int(t[(n - 1) % length])
