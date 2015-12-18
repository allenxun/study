class Solution(object):
    def plusOne(self, digits):  
        """ 
        :type digits: List[int] 
        :rtype: List[int] 
        """  
        dig = 1  
        for i in range(len(digits)-1,-1,-1):  
            if digits[i]+dig>9:  
                digits[i] = 0  
            else :   
                digits[i] = digits[i]+dig  
                dig = 0  
        if dig == 1:  
            digits.insert(0,1)  
        return digits 
