class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        ans = []
        cur = []
        def palindrome(s,l,r):
            
            while (l<r):
                if s[l] != s[r]: 
                    return False
                l += 1
                r -= 1
            return True


        def dfs(i):
            if i >= len(s):
                ans.append(cur.copy())
                return

            for j in range(i,len(s)):
                if palindrome(s,i,j):
                    cur.append(s[i:j+1])
                    dfs(j+1)
                    cur.pop()

        dfs(0)
        return ans

        
