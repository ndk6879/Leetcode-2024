class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        adict = Counter(nums)
        print('adict:',adict)

        arr = [[] for _ in range(len(nums)+1)]
        for num in adict:
            index = adict[num]
            arr[index].append(num)

        print('arr:',arr)

        ans = []
        for i in range(len(arr)-1,-1,-1):
            for num in arr[i]:
                ans.append(num)
                k -= 1
                if k == 0:
                    return ans