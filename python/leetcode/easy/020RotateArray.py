class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate0(self, nums, k):
        newk = len(nums)-k%len(nums)
        for i in range(0,newk):
            nums.append(nums[0])
            nums.remove(nums[0])

    def rotate1(self, nums, k):
        k = k%len(nums)
        self.reverse(nums, 0, n - k)
        self.reverse(nums, n - k, n)
        self.reverse(nums, 0, n)

    def reverse(self, nums, start, end):
        for x in range(start, (start + end) / 2):
            nums[x] ^= nums[start + end - x - 1]
            nums[start + end - x - 1] ^= nums[x]
            nums[x] ^= nums[start + end - x - 1]

if __name__=="__main__":
    a = Solution()
    test = [[1,2,3,4,5,6,7],[1,2],[1,2,3]]
    for i in test:
        print "Original   ",i
        a.rotate0(i,4)
        print "rotate0"+"    ",i

    test = [[1,2,3,4,5,6,7],[1,2],[1,2,3]]
    for i in test:
        print "Original   ",i
        a.rotate0(i,4)
        print "rotate1"+"    ",i
