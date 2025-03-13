class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        
        res = ''
        for string in strs:
            res += str(len(string)) + '#' + string

        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        
        i = 0
        j = 0
        ans = []
        while (i < len(s)):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            string = s[j+1:j+1+length]
            ans.append(string)
            i = j + 1 + length
        return ans




# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))