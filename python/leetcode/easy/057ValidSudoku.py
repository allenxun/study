import copy
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        matrix = []
        col = []
        temp = copy.deepcopy(board)
        tempcol = copy.deepcopy(board)
        #row
        for i in range(0,9):
            if self.check(temp[i]):
                continue
            else:
                return False
            
        #col
        for i in range(0,9):
            for j in range(0,9):
                col.append(tempcol[j][i])
            if self.check(col):
                col = []
                continue
            else:
                return False

        #matrix
        for i in range(0,9,3):
            for j in range(0,9,3):
                for k in range(0,3):
                    for h in range(0,3):
                        matrix.append(board[i+k][j+h])
                if self.check(matrix):
                    matrix = []
                    continue
                else:
                    return False

        return True
               
    def check(self,nums):
        while "." in nums:
            nums.remove(".")
        sets = set(nums)
        if len(sets) == len(nums):
            return True
        else:
            return False


if __name__ == "__main__":
    test=[
        ["2","3","4","5","6","7","8","9","1"],
        ["1",".",".",".",".",".",".",".","."],
        ["9",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".",".","."],
        ["6",".",".",".",".",".",".",".","."],
        ["2",".",".",".",".",".",".",".","."],
        ["8",".",".",".",".",".",".",".","."],
        ["4",".",".",".",".",".",".",".","."],
        ["3",".",".",".",".",".",".",".","."],
        ]
    a = Solution()
    print a.isValidSudoku(test)
