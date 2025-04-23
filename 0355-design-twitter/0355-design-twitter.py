from collections import defaultdict, OrderedDict
import heapq

class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.following = defaultdict(set)  # 이름 변경
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.count, tweetId))
        self.count += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId] | {userId}
        heap = []
        for user in users:
            for time, tid in self.posts[user]:
                heapq.heappush(heap,(-time,tid))
        
        ans = []

        while heap and len(ans) < 10:
            cur = heapq.heappop(heap)
            ans.append(cur[1])
        return ans


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)