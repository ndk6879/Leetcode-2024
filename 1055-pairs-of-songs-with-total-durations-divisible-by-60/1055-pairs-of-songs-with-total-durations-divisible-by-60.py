class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        '''
        1. get all combinations of times
        2. check if divisible by 60

        or 
        two pointer, binart search, sliding window
        '''
        
        remainder = [0] * 60  # 각 노래의 시간을 60으로 나눈 나머지를 저장하는 배열
        count = 0  # 결과로 반환할 쌍의 개수

        for t in time:
            mod = t % 60  # 노래 시간을 60으로 나눈 나머지
            complement = (60 - mod) % 60  # 60과 더해서 60의 배수가 되는 나머지 값을 계산
            
            count += remainder[complement]  # complement가 존재하면 그 수만큼 쌍을 더함
            remainder[mod] += 1  # 현재 노래의 나머지를 카운트 배열에 추가
        
        return count  # 최종 쌍의 개수를 반환