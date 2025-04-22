from collections import defaultdict, OrderedDict
from typing import List

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.posts = defaultdict(OrderedDict)  # userId: OrderedDict[tweetId: timestamp]
        self.following = defaultdict(set)      # userId: set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId][tweetId] = self.timestamp
        self.timestamp += 1
        self.posts[userId].move_to_end(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        candidates = []

        # 자기 자신 + 팔로우한 사람들의 최근 트윗 수집
        user_ids = self.following[userId] | {userId}
        for uid in user_ids:
            for tweetId, ts in reversed(self.posts[uid].items()):
                candidates.append((ts, tweetId))

        # 최신순 정렬 후 상위 10개
        candidates.sort(reverse=True)
        return [tweetId for _, tweetId in candidates[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
