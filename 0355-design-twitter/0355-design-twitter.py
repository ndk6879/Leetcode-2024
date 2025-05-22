from collections import defaultdict

class Twitter:

    def __init__(self):
        self.post = defaultdict(list)   #{ postID : [[0, tweetID1] , [1, tweetID2]]
        self.following = defaultdict(set)  #{ userID : {follower1, follower2} }
        self.count = 0

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post[userId].append([self.count , tweetId])
        self.count += 1
    

        

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId] | {userId} # every userID

        posts = []
        for user in users:
            for time, tid in self.post[user]:
                posts.append([-1 * time , tid])
        

        heapq.heapify(posts)
        n = 10
        ans = []
        while posts and n > 0:
            tid = heapq.heappop(posts)[1]
            ans.append(tid)
            n -= 1

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