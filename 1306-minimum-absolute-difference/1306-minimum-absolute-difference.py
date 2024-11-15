class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        adict = {}
        arr.sort()
        for i in range(1,len(arr)):
            diff = arr[i] - arr[i-1]
            if diff not in adict:
                adict[diff] = [ [arr[i-1],arr[i]] ]
            else:
                adict[diff].append([arr[i-1],arr[i]]) 
        return adict[min(adict.keys())]