class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        temps = {}
        for i in nums:
            if temps.has_key(i):
                temps[i]+=1
            else:
                temps[i]=1
        arr1 = sorted(temps.iteritems(), key=lambda asd:asd[1], reverse=True)
        arr2 = []
        for key in range(len(arr1)):
            arr2.append(arr1[key][0])
        return arr2[0:k]
        