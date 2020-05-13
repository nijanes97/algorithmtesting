class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend == -2147483648 and divisor == -1:
            return abs(-2147483648) - 1
        if (dividend < 0 and divisor > 0) or (dividend >= 0 and divisor < 0):
            sign = -1
        else:
            sign = 1
            
        tempdivid = abs(dividend)
        tempdivis = abs(divisor)
        
        if tempdivid == tempdivis:
            return sign
        
        answer = 0
        temp = 0
        
        for i in range(31, -1, -1):
            if temp + (tempdivis << i) <= tempdivid:
                temp += tempdivis << i
                answer |= 1 << i
                
        return sign * answer