class Solution:
    def isValid(self, s: str) -> bool:
        
        '''
        use stack variable
        if s is opening, add
        if closing, pop to get. last and check if match
        - not match, return false
        - return if []
        '''

        cur = []
        
        char = {
            ')' : '(' ,
            '}' : '{',
            ']' : '[' 
        }

        for c in s:
            if c in char.values():
                cur.append(c)
            
            elif c in char.keys():
                if cur == [] or char[c] != cur.pop():
                    return False
        
        return cur == []