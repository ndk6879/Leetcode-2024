from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        #1. create counter to count each # of elements 
        #2. sort the hand
        #3. use for loop to iterate over and check if there's next elment at each index


        counter = Counter(hand)
        hand.sort()
        
        for num in hand:
            if counter[num]:
                for i in range(num,num+groupSize):
                    if not counter[i]:
                        return False

                    counter[i] -= 1
        
        return True