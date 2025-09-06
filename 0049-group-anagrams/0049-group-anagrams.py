class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        hashMap = {}
        for string in strs:

            arr = [0] * 26
            for c in string:
                arr[ord(c) - ord('a')] += 1

            if tuple(arr) not in hashMap:
                hashMap[tuple(arr)] = [string]
            else:
                hashMap[tuple(arr)].append(string)
        
        return list( hashMap.values() )