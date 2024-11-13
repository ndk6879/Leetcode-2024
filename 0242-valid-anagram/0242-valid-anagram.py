class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        #1. compare if backwards is same
        #2. check if they have same dtionary to comapre same # of chr. 
        '''
        
        dictS = {}
        dictT = {}

        for let in s:
            if let not in dictS:
                dictS[let] = 1
            else:
                dictS[let] += 1
            
        for let in t:
            if let not in dictT:
                dictT[let] = 1
            else:
                dictT[let] += 1

        return dictT == dictS
        