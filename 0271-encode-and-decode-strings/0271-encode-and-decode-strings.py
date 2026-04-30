class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        ans = ''

        for string in strs:
            ans += str(len(string)) + '#' + string
        print('ans:',ans)
        return ans
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        
        '''
        - use two pointer l,r to find the location of digits before #
        '''

        l,r = 0,0
        ans = []
        while(r < len(s)):

            while(s[r] != '#'):
                r += 1
            
            length = int(s[l:r])
            string = s[r+1:r+1+length]
            ans.append(string)
            
            r = r + 1 + length
            l = r
        return ans



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))