

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num,0) + 1

        print('hashMap:',hashMap)

        arr = [[] for _ in range(len(nums))]

        for key,v in hashMap.items():
            arr[v-1].append(key)

        print('arr:',arr)

        ans = []
        for i in range(len(arr) -1 , -1 , -1):
            cur = arr[i]
            print('cur:',cur)
            while cur:
                tmp = cur.pop()
                ans.append(tmp)
                print('ans:',ans,k)
                k-= 1
            if k == 0:
                return ans