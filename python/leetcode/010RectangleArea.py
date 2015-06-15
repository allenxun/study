class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        area1 = (C-A)*(D-B)
        area2 = (G-E)*(H-F)
        a = max(A,E)
        b = max(B,F)
        c = min(C,G)
        d = min(D,H)

        area3 = (d-b)*(c-a)

        if d<=b or c<=a:
            return area1+area2
        else:
            return area1+area2-area3

if __name__ == "__main__":
    a = Solution()
    test = [[-2, -2, 2, 2, 3, 3, 4, 4],[-3,0,3,4,0,-1,9,2]]
    for i in test:
        print a.computeArea(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
