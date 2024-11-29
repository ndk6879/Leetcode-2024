class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        arr = []
        for i in range(len(text1)+1):
            tmp = []
            for j in range(len(text2)+1):
                tmp.append(0)
            arr.append(tmp)

        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    arr[i][j] = arr[i+1][j+1]+1
                else:
                    arr[i][j] = max(arr[i][j+1],arr[i+1][j])
        for i in arr:
            print(i)
        return arr[0][0]