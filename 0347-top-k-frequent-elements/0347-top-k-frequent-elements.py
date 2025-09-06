class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # { num : occurrence }
        # [] * len(nums)
        # for loop in backwards to find the most freq one

        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num,0) + 1

        arr = [[] for _ in range(len(nums))]

        for num, occur in hashMap.items():
            print(num,occur)
            arr[occur-1].append(num)


        ans = []

        for i in range(len(arr)-1,-1,-1):
            
            cur = arr[i]
            
            while len(cur) > 0:
                tmp = cur.pop()
                ans.append(tmp)
                k -= 1
                if k == 0: return ans