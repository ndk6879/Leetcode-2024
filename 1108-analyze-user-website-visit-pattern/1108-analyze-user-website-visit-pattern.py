from collections import defaultdict, Counter
from itertools import combinations

class Solution:
    def mostVisitedPattern(self,username, timestamp, website):
        # Step 1: 정렬
        data = sorted(zip(timestamp, username, website))
        
        # Step 2: 유저별 방문 기록 모으기
        user_visits = defaultdict(list)
        for time, user, site in data:
            user_visits[user].append(site)
        
        # Step 3: 유저별 3-sequence 만들기
        sequence_count = Counter()
        for user, sites in user_visits.items():
            # 유저별로 unique한 sequence만 set으로 만들기
            sequences = set(combinations(sites, 3))
            for seq in sequences:
                sequence_count[seq] += 1
        
        # Step 4: 가장 많이 등장한 sequence 리턴 (사전순 tie 처리 자동)
        return list(min([seq for seq, cnt in sequence_count.items() if cnt == max(sequence_count.values())]))
