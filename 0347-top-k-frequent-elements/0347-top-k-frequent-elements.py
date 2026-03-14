class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        '''
        - 1. create hashMap and count how many each element exists
        - 2. create Array with len(nums+1) and assign elements from nums at index where each index is key in hashMap
        -3. count in backwards
        '''

        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num,0) + 1
            
        arr = [[] for _ in range(len(nums)+1)]

        for b,v in hashMap.items():
            arr[v].append(b)
        
        ans = []
        print(arr)
        for i in range(len(arr)-1,-1,-1):

            while len(arr[i]) > 0:
                cur = arr[i].pop()
                ans.append(cur)
                k -=1 
                if k == 0:return ans

