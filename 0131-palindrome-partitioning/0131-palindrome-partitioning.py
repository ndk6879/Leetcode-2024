class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []

        def dfs(i,path):
            if len(s) == i:
                ans.append(path[:])
                return


            for j in range(i,len(s)):
                if self.palindrome(s,i,j):
                    path.append(s[i:j+1])
                    dfs(j+1,path)
                    path.pop()
                    
        dfs(0,[])

        return ans

    def palindrome(self, s, l, r):

        while l <= r:
            if s[l] != s[r]: return False

            l += 1
            r -= 1
        return True