import os


class shudu():
    def __init__(self, all,clear):
        self.all = all
        self.clear = clear
        self.baoli = [[] for i in range(9)]
    
    def get_row(self,i):
    	return self.all[i]

    def get_col(self,j):
    	col = []
        for i in range(0,9):
            col.append(self.all[i][j])
        return col

    def get_gezi(self,i,j):
    	gezi = [[[] for i in range(3)] for i in range(3)]
        for m in range(0,9,3):
    	    for n in range(0,9,3):
            	for p in range(0,3):
                    for q in range(0,3):
                     	gezi[m/3][n/3].append(test[m+p][n+q])

        return gezi[i/3][j/3]

    def get_all_num(self):
        for i in range(0,9):
            for j in range(0,9):
                if shudu[i][j] == 0:
	                self.clear = list(set(self.clear[i][j]).difference(set(self.get_row(i))).difference(set(self.get_col(j))).difference(set(self.get_gezi(i,j))))
		else:
		    self.clear[i][j] = 0

    def change_all(self):
        for i in range(0,9):
            for j in range(0,9):
    	        if len(clear[i][j])==1:
    	            self.all[i][j] == self.clear[i][i][0]
                    self.clear[i][j] = 0
    def is_clear(self):
        zero = 0
        one = 0
        more = 0
        for i in range(0,9):
            for j in range(0,9):
                if self.clear[i][j] == 0:
    	            zero = zero+1
    		elif len(self.clear[i][j]) == 1:
    		    one = one+1
    		else:
    		    more = more+1
    	if zero == 81:
            return 1
    	elif one == 0:
    	    return 2
    	else:
    	    return 3

    def isValidSudoku(self):
    	rows = [list(lst[::]) for lst in self.all]
    	columns = [[lst[idx] for lst in self.all] for idx in range(9)]
    	blocks_origin = [self.all[row][column] for x in [[0, 1, 2], [3, 4, 5], [6, 7, 8]] for y in [[0, 1, 2], [3, 4, 5], [6, 7, 8]] for row in x for column in y]
    	blocks = [[blocks_origin[row * 9 + column] for column in range(9)] for row in range(9)]
    	check = lambda lst: all([lst.count(x) == 1 for x in lst if x != '.'])
    	return all([check(x) for style in (rows, columns, blocks) for x in style])

    def is_end(self):
    	end=0
    	for i in range(0,9):
            for j in range(0,9):
    	        if self.all == 0:
    		        end = end+1
     	if end == 0:
            return True
    	else:
    	    return False


if __name__ == '__main__':
    arr = [[],[],[],[],[],[],[],[],[]]
    for i in range(0,9):
        for j in range(0,9):
            arr[i].append([1,2,3,4,5,6,7,8,9])

    test = [  
    	[0, 0, 0, 3, 0, 0, 5, 0, 0],  
    	[0, 0, 0, 0, 4, 0, 0, 8, 0],  
    	[0, 1, 0, 5, 7, 9, 4, 0, 3],  
    	[5, 0, 2, 0, 0, 0, 0, 0, 0],  
    	[0, 0, 4, 0, 0, 0, 1, 0, 0],  
    	[0, 0, 0, 0, 0, 0, 9, 0, 7],  
    	[4, 0, 7, 9, 1, 5, 0, 3, 0],  
    	[0, 6, 0, 0, 8, 0, 0, 0, 0],  
    	[0, 0, 1, 0, 0, 3, 0, 0, 0],  
	]

    eg1 = shudu(test,arr)
 	
    if eg1.isValidSudoku():
    	while eg1.is_clear()==2 or eg1.is_clear()==1:
            eg1.get_all_num()
            eg1.change_all()
            eg1.get_all_num()
 	    if eg1.is_end():
 	        print eg1.all
 	    else:
 	        print eg1.clear
 	else:
            print "It's not shudu"





