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
        
from collections import Counter
def frequencyQueries(queries):
    # Write your code here
    # keeps a tally of which numbers have been inserted
    numCounter = Counter()
    # keeps a tally of which frequencies are currently present in the collection
    frequencyCounter = Counter()
    queryReturns = []

    for query, value in queries:
        if query == 1:
            # stores the number being added to numCounter, then adds 1 to the frequency counter for that frequency
            frequencyCounter[numCounter[value]] -= 1
            numCounter[value] += 1
            frequencyCounter[numCounter[value]] += 1
        elif query == 2:
            if numCounter[value] > 0:
                # updates the stored numbers and the frequencies if the number exists in the collection
                frequencyCounter[numCounter[value]] -= 1
                numCounter[value] -= 1
                frequencyCounter[numCounter[value]] += 1   
        elif query == 3:
            # adds 1 or 0 to the return arr if the frequency exists
            if frequencyCounter[value] > 0:
                queryReturns.append(1)
            else:
                queryReturns.append(0)

    return queryReturns