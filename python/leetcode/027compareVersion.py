class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        if version1==version2:
            return 0
        int1 = 0
        changeVersion1 = ""
        int2 = 0
        changeVersion2 = ""
        if "." in version1:
            for i in range(len(version1)):
                if version1[i] == ".":
                    int1 = int(version1[:i])
                    changeVersion1 = version1[i+1:]
                    break
                
        else:
            int1 = int(version1)
            changeVersion1 = "0"
        
        if "." in version2:
            for i in range(len(version2)):
               if version2[i] == ".":
                    int2 = int(version2[:i])
                    changeVersion2 = version2[i+1:]
                    break
               
        else:
            int2 = int(version2)
            changeVersion2 = "0"

        if int1>int2:
            return 1
        if int1<int2:
            return -1
        if int1==int2:
            return self.compareVersion(changeVersion1,changeVersion2)


if __name__ == "__main__":
    test=[["1.2","1.4"],["1.1","1.1"],["1.1.2","1.2.1"],["1.20","1.2.0"]]
    a = Solution()
    for i in test:
        print a.compareVersion(i[0],i[1])
