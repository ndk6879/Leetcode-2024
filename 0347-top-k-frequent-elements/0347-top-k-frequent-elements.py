
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        adict = {}
        for num in nums:
            if num not in adict:
                adict[num] = 0
            else:
                adict[num] += 1
        
        arr = [[] for _ in range(len(nums))]

        for num in adict:
            occurrence = adict[num]
            arr[occurrence].append(num)


        ans = []
        for i in range(len(arr)-1,-1,-1):
            if len(arr[i]) > 0:
                while arr[i]:
                    cur = arr[i].pop()
                    ans.append(cur)
                    k -= 1
                    if k == 0: return ans
